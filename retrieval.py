
from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# ==========================================
# STEP 1: Define project directory
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

VECTOR_STORE_DIR = BASE_DIR / "VectorStore"


# ==========================================
# STEP 2: Verify ChromaDB directory
# ==========================================

if not VECTOR_STORE_DIR.exists():

    raise FileNotFoundError(
        f"VectorStore directory not found: {VECTOR_STORE_DIR}"
    )


# ==========================================
# STEP 3: Load embedding model
# ==========================================

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ==========================================
# STEP 4: Connect to existing ChromaDB
# ==========================================

vector_store = Chroma(

    collection_name="gitam_student_assistant",

    embedding_function=embedding_model,

    persist_directory=str(VECTOR_STORE_DIR)

)


# ==========================================
# STEP 5: Create retriever
# ==========================================

retriever = vector_store.as_retriever(

    search_kwargs={"k": 3}

)


# ==========================================
# STEP 6: Test retrieval
# ==========================================

if __name__ == "__main__":

    print("VectorStore location:", VECTOR_STORE_DIR)

    print("Collection count:", vector_store._collection.count())

    question = "What is the attendance requirement?"

    results = retriever.invoke(question)

    print("\nRetrieved documents:", len(results))

    for doc in results:

        print("\nDOCUMENT CONTENT:")
        print(doc.page_content)

        print("\nDOCUMENT SOURCE:")
        print(doc.metadata.get("source", "Unknown source"))

        print("\n--------------------")
