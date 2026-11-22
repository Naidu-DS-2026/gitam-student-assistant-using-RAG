
# Import already-loaded documents
from load_documents import documents

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

# Step 2: Split documents into chunks
chunks = text_splitter.split_documents(documents)

# Step 3: Display results
print("Total documents:", len(documents))
print("Total chunks:", len(chunks))

# Step 4: Display first 3 chunks
for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- CHUNK {i+1} ---")
    print("Source:", chunk.metadata["source"])
    print("Content:", chunk.page_content)
