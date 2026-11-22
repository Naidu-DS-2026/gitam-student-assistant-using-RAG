
from chunk_documents import chunks
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Step 1: Load the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 2: Create ChromaDB vector store
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="gitam_student_assistant",
    persist_directory="./VectorStore"
)

print("Documents stored:", len(chunks))
print("ChromaDB storage completed successfully!")
