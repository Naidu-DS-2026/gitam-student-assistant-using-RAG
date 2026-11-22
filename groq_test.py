
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Check whether API key is loaded
if not api_key:
    print("ERROR: Groq API key not found!")
else:
    print("API key loaded successfully!")

    try:
        # Initialize Groq
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0.3,
            api_key=api_key
        )

        # Test LLM
        response = llm.invoke(
            "What is Artificial Intelligence?"
        )

        print("\nGroq Response:")
        print(response.content)

    except Exception as e:
        print("\nERROR DETAILS:")
        print(type(e).__name__)
        print(str(e))
