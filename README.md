Website Link :- https://gitam-student-assistant-bot.streamlit.app/

# 🎓 GITAM SAGE – Smart Academic Guidance Engine

### An AI-Powered Academic Assistant Using Retrieval-Augmented Generation (RAG)

<p align="center">
  <strong>Intelligent Academic Guidance | Context-Aware Conversations | Knowledge-Based Responses</strong>
</p>

---

## 📌 1. Project Overview

**GITAM SAGE (Smart Academic Guidance Engine)** is an AI-powered academic assistance chatbot designed to help GITAM students access academic information through a conversational interface.

Students frequently need information about university regulations, attendance requirements, examinations, admissions, academic procedures, student services, and placement-related activities. Finding this information across different documents and resources can be time-consuming.

GITAM SAGE addresses this challenge by combining **Retrieval-Augmented Generation (RAG)** with Large Language Models (LLMs). It retrieves relevant information from an indexed knowledge base and generates context-aware responses using an LLM.

The application provides an interactive Streamlit interface where students can ask questions in natural language and receive responses based on the information available in the knowledge base.

---

## 🎯 2. Problem Statement

Students often face difficulties accessing accurate and relevant academic information because:

- Academic information may be distributed across multiple documents and resources.
- Students spend considerable time searching for specific academic policies and procedures.
- Finding relevant information in lengthy documents can be difficult.
- Repeated queries about attendance, examinations, and academic regulations create unnecessary effort.
- Traditional keyword-based searching does not always understand the actual meaning of a student's question.
- Students need a convenient way to ask follow-up questions and receive contextual explanations.

### Proposed Solution

GITAM SAGE provides a centralized conversational academic assistance system that:

1. Processes academic information and stores it in a searchable vector database.
2. Understands student queries using semantic embeddings.
3. Retrieves relevant document chunks from the knowledge base.
4. Uses an LLM to generate answers grounded in retrieved information.
5. Maintains conversational context to support follow-up questions.
6. Provides an easy-to-use web interface through Streamlit.

---

## 🎯 3. Project Objectives

- Develop an AI-powered academic assistance chatbot for GITAM students.
- Implement a complete Retrieval-Augmented Generation pipeline.
- Convert academic documents into searchable vector representations.
- Perform semantic search using Hugging Face embeddings.
- Store and retrieve document embeddings using ChromaDB.
- Integrate Groq LLM for natural-language response generation.
- Implement conversational memory for contextual interactions.
- Build a user-friendly chatbot interface using Streamlit.
- Deploy the application online for public access.

---

## 🛠️ 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive chatbot frontend |
| LangChain | LLM application development and RAG orchestration |
| LangChain Core | Prompts, chains, and runnable components |
| Hugging Face | Text embedding model |
| Sentence Transformers | Semantic text embeddings |
| ChromaDB | Vector database |
| Groq | LLM inference |
| OpenAI-compatible Groq model | Natural-language response generation |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and source-code hosting |
| Streamlit Community Cloud | Application deployment |

### Models Used

**Embedding Model**

`sentence-transformers/all-MiniLM-L6-v2`

Used to convert text documents and user queries into numerical vector representations for semantic similarity search.

**Language Model**

`openai/gpt-oss-120b` through Groq.

Used to generate natural-language responses based on the retrieved context and conversation history.

---

## 🧠 5. Core Concept – Retrieval-Augmented Generation (RAG)

GITAM SAGE uses Retrieval-Augmented Generation to improve the relevance of LLM responses by providing information retrieved from an external knowledge base.

### How RAG Works

**Step 1 – Document Loading**

Academic documents are loaded into the application using suitable document loaders.

**Step 2 – Text Splitting**

Documents are divided into smaller chunks to make retrieval more efficient.

**Step 3 – Embedding Generation**

The Hugging Face embedding model converts each text chunk into a numerical vector.

**Step 4 – Vector Storage**

The generated embeddings and associated document content are stored in ChromaDB.

**Step 5 – User Query**

A student enters a question through the Streamlit interface.

**Step 6 – Semantic Retrieval**

The question is converted into an embedding, and the retriever searches ChromaDB for relevant document chunks.

**Step 7 – Contextual Prompt Construction**

The retrieved information is combined with the user question and relevant conversation context.

**Step 8 – LLM Response Generation**

The Groq-hosted language model generates a response using the supplied context.

**Step 9 – Response Display**

The generated answer is displayed in the Streamlit chatbot interface.

---

## 🏗️ 6. System Architecture

```text
             STUDENT
                |
                v
       STREAMLIT CHAT INTERFACE
                |
                v
          USER QUESTION
                |
                v
        RAG APPLICATION
                |
                v
       HUGGING FACE EMBEDDINGS
                |
                v
          CHROMADB SEARCH
                |
                v
       RETRIEVED DOCUMENT CHUNKS
                |
                v
       PROMPT + CONVERSATION
              CONTEXT
                |
                v
          GROQ LLM
                |
                v
        GENERATED RESPONSE
                |
                v
        STREAMLIT INTERFACE
                |
                v
             STUDENT
```

### Knowledge Base Indexing Pipeline

```text
Academic Documents
        |
        v
Document Loading
        |
        v
Text Splitting
        |
        v
Embedding Generation
        |
        v
ChromaDB Vector Storage
        |
        v
      Retriever
```

---

## ⚙️ 7. Key Features

### 7.1 AI-Powered Academic Assistance
Students can ask natural-language questions about academic information available in the indexed knowledge base.

### 7.2 Retrieval-Augmented Generation
Retrieves relevant document content before generating an answer, helping ground responses in the available information.

### 7.3 Semantic Search
Uses sentence embeddings to identify relevant content based on meaning rather than relying only on exact keyword matching.

### 7.4 Conversational Memory
Maintains conversation context to support follow-up questions within a chat session.

### 7.5 Interactive Chat Interface
Provides a Streamlit-based interface for asking questions and viewing responses.

### 7.6 Source-Aware Responses
The application can display retrieved document sources alongside generated answers, depending on the available source metadata.

### 7.7 Cloud Deployment
The application is designed to run through Streamlit Community Cloud.

---

## 📂 8. Project Structure

```text
RAG_END_2_END/
│
├── app.py
│
├── rag_with_memory.py
├── retrieval.py
│
├── load_documents.py
├── chunk_documents.py
├── create_embeddings.py
├── store_vectors.py
│
├── prompt_template.py
├── rag_chain.py
├── llm_chain.py
├── memory_test.py
│
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── VectorStore/
│   ├── chroma.sqlite3
│   └── [ChromaDB index files]
│
├── requirements.txt
├── .gitignore
└── README.md
```

### File Descriptions

| File / Directory | Responsibility |
|---|---|
| `app.py` | Main Streamlit application |
| `rag_with_memory.py` | RAG pipeline with conversational memory |
| `retrieval.py` | Embedding model, vector database connection, and retriever |
| `load_documents.py` | Loads source documents |
| `chunk_documents.py` | Splits documents into smaller chunks |
| `create_embeddings.py` | Generates document embeddings |
| `store_vectors.py` | Stores vectors in ChromaDB |
| `prompt_template.py` | Defines prompt instructions |
| `rag_chain.py` | RAG chain implementation |
| `llm_chain.py` | LLM chain implementation |
| `memory_test.py` | Tests conversational memory |
| `Data/Raw/` | Original source documents |
| `Data/Processed/` | Processed document data |
| `VectorStore/` | Persisted ChromaDB vector database |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes sensitive and unnecessary files |

---

## 💻 9. Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the selected dependencies.
- Git.
- A Groq API key.
- Internet connectivity for API access and initial model downloads.

### Step 1 – Clone the Repository

```bash
git clone https://github.com/Naidu-DS-2026/gitam-student-assistant-using_langchain.git
```

### Step 2 – Navigate to the Project Directory

```bash
cd gitam-student-assistant-using_langchain
```

### Step 3 – Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 4 – Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5 – Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Replace the placeholder with your own API key.

**Important:** Never upload `.env` or expose your API key on GitHub.

### Step 6 – Run the Application

```bash
streamlit run app.py
```

The application will start locally and provide a URL in your terminal.

---

## 🔐 10. Environment Configuration

The project requires a Groq API key to communicate with the language model.

For local development:

- Store the API key in `.env`.
- Load the key securely through environment variables.
- Exclude `.env` from version control.

For Streamlit Community Cloud:

1. Open your deployed application.
2. Navigate to app settings.
3. Open the Secrets section.
4. Add the following configuration:

```toml
GROQ_API_KEY = "your_actual_groq_api_key"
```

5. Save the configuration and restart the application if required.

Never commit API credentials to a public repository.

---

## ☁️ 11. Deployment

GITAM SAGE is designed for deployment using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project source code to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the project repository.
5. Choose `app.py` as the application entry point.
6. Configure the `GROQ_API_KEY` secret.
7. Deploy the application.
8. Verify the deployed application using sample academic questions.

**Deployment requirements:**

- Correct repository structure.
- Valid dependency configuration.
- Available ChromaDB vector store.
- Correct API credentials.
- Compatible Python and package versions.

---

## 🧪 12. Testing and Validation

The following test categories can be used to evaluate the application.

| Test Category | Example Question | Expected Behaviour |
|---|---|---|
| Attendance | What is the attendance requirement? | Retrieves relevant attendance information |
| Admissions | What are the B.Tech admission requirements? | Retrieves available admission information |
| Examinations | What is the supplementary examination process? | Provides relevant examination guidance |
| Student Services | How can I obtain a bonafide certificate? | Retrieves the related procedure if available |
| Semantic Search | Explain attendance rules in simple words | Finds semantically relevant content |
| Conversation Memory | Explain that in more detail | Uses the previous conversation context |
| Unknown Questions | Ask something absent from the knowledge base | Clearly indicates missing information |

### Important Validation Rule

The chatbot should not invent university policies or present unsupported information as official GITAM regulations. When relevant information is not available in the knowledge base, it should communicate that limitation.

---

## ⚠️ 13. Current Limitations

- Response quality depends on the accuracy and completeness of the indexed documents.
- The chatbot cannot reliably answer questions outside its available knowledge base.
- LLM-generated responses may require verification against official university sources.
- In-memory conversation history is temporary and is not automatically preserved across application restarts.
- Initial embedding model downloads can increase application startup time.
- Groq API availability, rate limits, and credentials affect response generation.
- Persisted local vector-store files must be available in the deployed environment.

---

## 🚀 14. Future Enhancements

The following improvements can extend the capabilities of GITAM SAGE:

1. **Persistent Chat History:** Store previous conversations using a database.
2. **Multi-Document Support:** Expand the knowledge base with additional academic documents.
3. **PDF Upload:** Allow authorized users to upload academic documents.
4. **Advanced Source Citations:** Display document names and page references for answers.
5. **Student Authentication:** Add secure student login functionality.
6. **Multilingual Support:** Support English and regional-language queries.
7. **Admin Dashboard:** Allow authorized administrators to manage knowledge-base documents.
8. **Improved Retrieval:** Experiment with hybrid search and reranking techniques.
9. **Feedback System:** Allow students to rate chatbot responses.
10. **Analytics Dashboard:** Analyze frequently asked questions and chatbot usage.

---

## 🎓 15. Learning Outcomes

Through this project, the following concepts and technologies are applied:

- Generative AI and Large Language Models.
- Retrieval-Augmented Generation (RAG).
- LangChain architecture and components.
- Prompt engineering.
- Text preprocessing and document chunking.
- Hugging Face sentence embeddings.
- Vector databases and semantic search.
- ChromaDB persistence and retrieval.
- Conversational memory.
- Streamlit application development.
- API integration and environment configuration.
- GitHub version control and cloud deployment.

---

## 👨‍💻 16. Developer

**Thirumala Naidu**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

**Technical Interests:**
- Data Science
- Machine Learning
- Generative AI
- Large Language Models
- Retrieval-Augmented Generation

**Connect with me:**

- LinkedIn: [Thirumala Naidu](https://www.linkedin.com/in/thirumala-naidu-b7a908289/)
- GitHub: [Naidu-DS-2026](https://github.com/Naidu-DS-2026)

---

## 📜 17. Disclaimer

GITAM SAGE is an independent academic assistance project developed for educational and informational purposes. It is not an official GITAM university application and is not affiliated with or endorsed by GITAM.

Responses depend on the documents included in its knowledge base and should be verified against official university communications for important academic decisions.

---

## ⭐ 18. Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Built with Python, LangChain, Hugging Face, ChromaDB, Groq, and Streamlit.**

