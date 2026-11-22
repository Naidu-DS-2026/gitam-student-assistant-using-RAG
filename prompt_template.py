
from langchain_core.prompts import ChatPromptTemplate

# Step 1: Create the chat prompt template
prompt = ChatPromptTemplate.from_messages([

    # System message
    (
        "system",
        """
        You are a GITAM University Student Assistant.

        Your responsibility is to answer student questions
        using only the provided GITAM document context.

        Rules:
        1. Answer only using the provided context.
        2. Do not invent information.
        3. Do not assume rules apply to every batch or programme.
        4. If the answer is not available in the context,
           clearly say that the information is not available
           in the provided documents.
        5. Give clear and simple answers.
        6. Preserve important dates, fees and conditions.
        """
    ),

    # Human message
    (
        "human",
        """
        GITAM Document Context:

        {context}

        Student Question:

        {question}
        """
    )

])

print("ChatPromptTemplate created successfully!")
