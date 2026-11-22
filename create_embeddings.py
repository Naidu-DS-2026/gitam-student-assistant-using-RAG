
from chunk_documents import chunks
from sentence_transformers import SentenceTransformer

# Step 1: Load the embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Step 2: Extract text from all chunks
texts = [chunk.page_content for chunk in chunks]

# Step 3: Convert text into embeddings
vectors = embedding_model.encode(texts)

# Step 4: Display results
print("Total chunks:", len(texts))
print("Embedding shape:", vectors.shape)

# Step 5: Display the first vector
print("\nFirst chunk embedding:")
print(vectors[0])

# Step 6: Display vector dimensions
print("\nVector dimensions:", len(vectors[0]))