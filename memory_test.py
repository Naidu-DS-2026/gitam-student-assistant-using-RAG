
from langchain_core.chat_history import InMemoryChatMessageHistory

# Step 1: Create chat history
chat_history = InMemoryChatMessageHistory()

# Step 2: Add student message
chat_history.add_user_message(
    "What is the attendance requirement?"
)

# Step 3: Add chatbot response
chat_history.add_ai_message(
    "The applicable attendance requirement depends on your programme regulations."
)

# Step 4: Add another student message
chat_history.add_user_message(
    "What happens if I don't meet it?"
)

# Step 5: Display complete conversation history
print("Conversation History:\n")

for message in chat_history.messages:
    print(type(message).__name__, ":", message.content)
