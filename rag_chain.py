
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from retrieval import retriever

# Load environment variables
load_dotenv()

# Initialize Groq
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a GITAM University Student Assistant.

    Answer using only the provided context.
    Do not invent information.
    If the answer is unavailable in the context,
    clearly say that it is not available.
    """),

    ("human", """
    Context:
    {context}

    Question:
    {question}
    """)
])

# Convert retrieved documents into text
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build RAG chain
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": lambda x: x
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Ask question
question = "What is the attendance requirement?"

response = rag_chain.invoke(question)

print("\nStudent Question:", question)
print("\nGITAM Assistant:", response)
