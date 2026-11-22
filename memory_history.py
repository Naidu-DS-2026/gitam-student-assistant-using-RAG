
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# STEP 1: Initialize Groq
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)

# STEP 2: Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful GITAM Student Assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# STEP 3: Create a normal chain
chain = prompt | llm

# STEP 4: Create a history storage dictionary
store = {}

# STEP 5: Create a function to retrieve session history
def get_session_history(session_id):

    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

# STEP 6: Wrap the chain with message history
conversation_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history"
)

# STEP 7: First question
response1 = conversation_chain.invoke(
    {"question": "What is attendance?"},
    config={"configurable": {"session_id": "student_1"}}
)

print("AI:", response1.content)

# STEP 8: Follow-up question
response2 = conversation_chain.invoke(
    {"question": "What happens if I don't meet it?"},
    config={"configurable": {"session_id": "student_1"}}
)

print("\nAI:", response2.content)

# STEP 9: Display conversation history
print("\nComplete Chat History:")

for message in get_session_history("student_1").messages:
    print(type(message).__name__, ":", message.content)
