
import os
import uuid
import streamlit as st
from dotenv import load_dotenv


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="GITAM SAGE | Student Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# 2. LOAD GROQ API KEY
# ==================================================

# Local VS Code: read the key from .env
load_dotenv()

# Streamlit Cloud: read the key from Secrets
try:
    cloud_api_key = st.secrets.get("GROQ_API_KEY")
    if cloud_api_key:
        os.environ["GROQ_API_KEY"] = cloud_api_key
except Exception:
    # Local .env may be used when Streamlit Secrets are unavailable
    pass

# Verify that an API key is available
if not os.getenv("GROQ_API_KEY"):
    st.error(
        "Groq API key is missing. "
        "For Streamlit Cloud, add GROQ_API_KEY in Settings > Secrets. "
        "For local execution, add it to your .env file."
    )
    st.stop()


# Import backend only after loading the API key
from rag_with_memory import ask_question


# ==================================================
# 3. CUSTOM CSS STYLING
# ==================================================

st.markdown("""
<style>
    .stApp {
        background-color: #f4f7fc;
    }

    [data-testid="stSidebar"] {
        background-color: #102b49;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 1250px;
    }

    div[data-testid="stChatMessage"] {
        background-color: white;
        border: 1px solid #e1e8f0;
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 12px;
    }

    div[data-testid="stChatInput"] {
        border-radius: 16px;
    }

    .stButton > button {
        border-radius: 12px;
        min-height: 55px;
        font-weight: 500;
        border: 1px solid #dce5f2;
        background-color: white;
        color: #173b62;
    }

    .stButton > button:hover {
        border-color: #3975e8;
        color: #245ac5;
    }

    h1, h2, h3 {
        color: #12345a;
    }

    [data-testid="stSidebar"] .stButton > button {
        background-color: #1d3b5b;
        border: 1px solid #34516f;
        color: white;
        text-align: left;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #294d70;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# ==================================================
# 4. INITIALIZE CHAT STATE
# ==================================================

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat_id" not in st.session_state:

    first_chat_id = str(uuid.uuid4())

    st.session_state.active_chat_id = first_chat_id

    st.session_state.chats[first_chat_id] = {
        "title": "New Chat",
        "messages": []
    }


# ==================================================
# 5. CREATE NEW CHAT
# ==================================================

def create_new_chat():

    new_chat_id = str(uuid.uuid4())

    st.session_state.chats[new_chat_id] = {
        "title": "New Chat",
        "messages": []
    }

    st.session_state.active_chat_id = new_chat_id


# ==================================================
# 6. LEFT SIDEBAR - CHAT HISTORY
# ==================================================

with st.sidebar:

    st.markdown("# 🎓 GITAM SAGE")

    st.caption("SMART ACADEMIC GUIDANCE ENGINE")

    st.divider()

    if st.button("＋ New Chat", use_container_width=True):

        create_new_chat()
        st.rerun()

    st.divider()

    st.markdown("### 💬 Recent Chats")

    for chat_id in reversed(list(st.session_state.chats.keys())):

        chat = st.session_state.chats[chat_id]

        title = chat["title"]

        if chat_id == st.session_state.active_chat_id:
            title = "● " + title

        if st.button(
            title,
            key=f"history_{chat_id}",
            use_container_width=True
        ):

            st.session_state.active_chat_id = chat_id
            st.rerun()

    st.divider()

    st.markdown("### 📚 Knowledge Base")

    st.caption(
        "Answers are generated using the GITAM documents "
        "loaded into the knowledge base."
    )

    st.divider()

    st.caption("GITAM SAGE | AI Student Assistant")

    st.caption(
        "Independent student project. "
        "Not an official GITAM University service."
    )


# ==================================================
# 7. GET ACTIVE CHAT
# ==================================================

active_chat_id = st.session_state.active_chat_id

active_chat = st.session_state.chats[active_chat_id]

messages = active_chat["messages"]


# ==================================================
# 8. MAIN HEADER
# ==================================================

st.title("🎓 GITAM Student Assistant")

st.write(
    "Your intelligent academic information assistant. "
    "Ask questions and explore information from the "
    "available GITAM documents."
)

st.divider()


# ==================================================
# 9. WELCOME SCREEN
# ==================================================

if not messages:

    st.markdown("## 👋 Welcome to GITAM SAGE")

    st.write(
        "How can I help you today? Ask about attendance, "
        "examinations, backlogs, scholarships, fees "
        "and admission refund policies."
    )

    st.markdown("### ✨ Try asking")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📅 What is the attendance requirement?",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What is the attendance requirement?"
            )
            st.rerun()

        if st.button(
            "🎓 What scholarships are available?",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What scholarships are available?"
            )
            st.rerun()

        if st.button(
            "🔄 How can I clear my backlogs?",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "How can I clear my backlogs?"
            )
            st.rerun()

    with col2:

        if st.button(
            "📝 Explain the examination rules",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "Explain the examination rules."
            )
            st.rerun()

        if st.button(
            "💰 Explain the tuition fee structure",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "Explain the tuition fee structure."
            )
            st.rerun()

        if st.button(
            "📄 How can I apply for revaluation?",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "How can I apply for revaluation?"
            )
            st.rerun()


# ==================================================
# 10. DISPLAY CHAT HISTORY
# ==================================================

for message in messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander("📚 View source documents"):

                    for source in sources:
                        st.write(f"📄 {source}")

            else:

                st.caption("No source documents were retrieved.")


# ==================================================
# 11. CHAT INPUT
# ==================================================

typed_question = st.chat_input(
    "Ask anything about GITAM rules, examinations and fees..."
)

pending_question = st.session_state.pop(
    "pending_question",
    None
)

question = typed_question or pending_question


# ==================================================
# 12. PROCESS STUDENT QUESTION
# ==================================================

if question:

    # Display student question
    with st.chat_message("user"):
        st.markdown(question)

    # Save user message
    messages.append({
        "role": "user",
        "content": question
    })

    # Generate chat title
    if active_chat["title"] == "New Chat":
        active_chat["title"] = question[:35]

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching GITAM documents and preparing your answer..."
        ):

            try:

                response = ask_question(
                    question,
                    active_chat_id
                )

                answer = response["answer"]

                # Extract source filenames
                source_docs = response.get("sources", [])

                sources = list(dict.fromkeys(
                    doc.metadata.get(
                        "source",
                        "Unknown source"
                    )
                    for doc in source_docs
                ))

                st.markdown(answer)

                if sources:

                    with st.expander("📚 View source documents"):

                        for source in sources:
                            st.write(f"📄 {source}")

                else:

                    st.warning(
                        "No source documents were retrieved. "
                        "Please verify the knowledge base."
                    )

                # Save assistant response
                messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as error:

                st.error(
                    f"Unable to generate an answer: {error}"
                )


# ==================================================
# 13. FOOTER
# ==================================================

st.divider()

st.caption(
    "GITAM SAGE | Powered by LangChain, ChromaDB, "
    "Hugging Face Embeddings and Groq."
)

st.caption(
    "Independent student project. Verify important academic "
    "decisions with the applicable official university regulations."
)
