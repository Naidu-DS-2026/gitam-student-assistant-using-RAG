
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Step 2: Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=api_key
)

# Step 3: Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a GITAM University Student Assistant.

        Answer using only the provided context.
        Do not invent information.
        If information is unavailable, say so.
        """
    ),
    (
        "human",
        """
        Context:
        {context}

        Student Question:
        {question}
        """
    )
])

# Step 4: Connect prompt and LLM
chain = prompt | llm

# Step 5: Provide sample input
response = chain.invoke({
    "context": "The example context says students must maintain 75% attendance.",
    "question": "What is the attendance requirement?"
})

# Step 6: Display answer
print(response.content)
