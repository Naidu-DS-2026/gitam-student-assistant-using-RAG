
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)

from langchain_core.chat_history import (
    InMemoryChatMessageHistory
)

from langchain_core.output_parsers import StrOutputParser

from retrieval import retriever


# ==========================================
# STEP 1: Load environment variables
# ==========================================

load_dotenv()


# ==========================================
# STEP 2: Initialize Groq LLM
# ==========================================


import os
import streamlit as st
from dotenv import load_dotenv

# Load local .env file when running in VS Code
load_dotenv()

# Read API key from Streamlit Cloud Secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except (KeyError, FileNotFoundError):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Verify API key availability
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Configure it in Streamlit Cloud Settings > Secrets."
    )

# Initialize Groq with the explicitly supplied key
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=GROQ_API_KEY
)



# ==========================================
# STEP 3: Question contextualization prompt
# ==========================================

contextualize_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are a question contextualization assistant.

        Given the previous conversation and the latest question,
        rewrite the latest question as a standalone question.

        If the question is already clear, return it unchanged.

        Do not answer the question.
        """
    ),

    MessagesPlaceholder(variable_name="chat_history"),

    ("human", "{question}")

])


# ==========================================
# STEP 4: Question rewriting chain
# ==========================================

contextualize_chain = (
    contextualize_prompt
    | llm
    | StrOutputParser()
)


# ==========================================
# STEP 5: Format retrieved documents
# ==========================================

def format_docs(docs):

    formatted_docs = []

    for i, doc in enumerate(docs, start=1):

        source = doc.metadata.get(
            "source",
            "Unknown source"
        )

        formatted_text = f"""
Source {i}: {source}

Content:
{doc.page_content}
"""

        formatted_docs.append(formatted_text)

    return "\n\n".join(formatted_docs)


# ==========================================
# STEP 6: Answer generation prompt
# ==========================================

answer_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are a GITAM University Student Assistant.

        Your responsibility is to answer student questions
        using only the retrieved GITAM document context.

        RULES:

        1. Answer only using the provided context.
        2. Do not invent information.
        3. Do not assume rules apply to every programme or batch.
        4. If information is unavailable in the context,
           clearly say it is not available in the provided documents.
        5. Give clear and student-friendly answers.
        6. Do not create unsupported policy details.
        """
    ),

    MessagesPlaceholder(variable_name="chat_history"),

    (
        "human",
        """
        Retrieved Context:

        {context}

        Student Question:

        {question}

        Provide an accurate answer using the retrieved context.
        """
    )

])


# ==========================================
# STEP 7: Retrieve relevant documents
# ==========================================

def retrieve_documents(inputs):

    # Get standalone question
    standalone_question = inputs["standalone_question"]

    # Retrieve documents from ChromaDB
    docs = retriever.invoke(standalone_question)

    # Prepare context
    context = format_docs(docs)

    # Return all required inputs
    return {

        "question": inputs["question"],

        "chat_history": inputs["chat_history"],

        "context": context,

        "sources": docs

    }


# ==========================================
# STEP 8: Build retrieval chain
# ==========================================

retrieval_chain = (

    RunnablePassthrough.assign(

        standalone_question=contextualize_chain

    )

    | RunnableLambda(retrieve_documents)

)


# ==========================================
# STEP 9: Generate answer and preserve sources
# ==========================================

complete_rag_chain = (

    retrieval_chain

    | RunnablePassthrough.assign(

        answer=(

            answer_prompt

            | llm

            | StrOutputParser()

        )

    )

)


# ==========================================
# STEP 10: Store conversation histories
# ==========================================

store = {}


def get_session_history(session_id):

    if session_id not in store:

        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


# ==========================================
# STEP 11: Add conversation memory
# ==========================================

conversation_rag = RunnableWithMessageHistory(

    complete_rag_chain,

    get_session_history,

    input_messages_key="question",

    history_messages_key="chat_history",

    output_messages_key="answer"

)


# ==========================================
# STEP 12: Function to display sources
# ==========================================

def display_sources(response):

    print("\n========== SOURCE DOCUMENTS ==========")

    sources = response["sources"]

    if not sources:

        print("No source documents retrieved.")

    else:

        displayed_sources = set()

        for doc in sources:

            source = doc.metadata.get(
                "source",
                "Unknown source"
            )

            if source not in displayed_sources:

                print(source)

                displayed_sources.add(source)



# ==========================================
# STEP 13: Function for Streamlit application
# ==========================================

def ask_question(question, session_id):

    response = conversation_rag.invoke(

        {
            "question": question
        },

        config={

            "configurable": {

                "session_id": session_id

            }

        }

    )

    return {
        "answer": response["answer"],
        "sources": response["sources"]
    }


# ==========================================
# STEP 14: Run standalone testing only
# ==========================================

if __name__ == "__main__":

    response = ask_question(
        "What is the attendance requirement?",
        "student_test"
    )

    print("\nANSWER:")
    print(response["answer"])

    print("\nSOURCES:")

    for doc in response["sources"]:
        print(doc.metadata.get("source", "Unknown source"))
