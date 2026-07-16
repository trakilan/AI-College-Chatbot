import os
import chromadb
from sentence_transformers import SentenceTransformer

print("Current Working Directory:")
print(os.getcwd())

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma database
client = chromadb.PersistentClient(path="database")

collection = client.get_or_create_collection(
    name="college_information"
)

# Data folder
DATA_FOLDER = "data"

documents = []

# Read all text files
for filename in os.listdir(DATA_FOLDER):

    if filename.endswith(".txt"):

        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as file:

            text = file.read()

            documents.append(text)

# Split into chunks
chunks = []

chunk_size = 500

for document in documents:

    for i in range(0, len(document), chunk_size):

        chunks.append(document[i:i+chunk_size])

# Create embeddings
embeddings = embedding_model.encode(chunks).tolist()

# Store in ChromaDB
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)

print("Knowledge Base Created Successfully!")