
from langchain_community.document_loaders import DirectoryLoader, Docx2txtLoader

# Step 1: Specify the folder containing GITAM documents
data_path = "Data/Raw"

# Step 2: Create the document loader
loader = DirectoryLoader(
    path=data_path,
    glob="0[1-6]_*.docx",
    loader_cls=Docx2txtLoader,
    show_progress=True
)

# Step 3: Load all six documents
documents = loader.load()

# Step 4: Display the number of loaded documents
print("Total documents loaded:", len(documents))

# Step 5: Display document details
for doc in documents:
    print("\n--------------------------------")
    print("Source:", doc.metadata["source"])
    print("Content length:", len(doc.page_content))
    print("Content preview:")
    print(doc.page_content[:300])
