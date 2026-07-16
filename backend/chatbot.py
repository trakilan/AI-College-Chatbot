import chromadb
from sentence_transformers import SentenceTransformer

from google import genai
from config import GEMINI_API_KEY

# -------------------------
# Gemini Client
# -------------------------
client = genai.Client(api_key=GEMINI_API_KEY)




# -------------------------
# Load Chroma Database
# -------------------------
db = chromadb.PersistentClient(path="database")

collection = db.get_collection("college_information")

# -------------------------
# Load Embedding Model
# -------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
def search_knowledge(question):

    question_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)


def get_chat_response(question):

    # Search the knowledge base
    context = search_knowledge(question)

    prompt = f"""
You are an AI Assistant for Thiagarajar College of Engineering (TCE).

You must answer ONLY using the college information provided below.

If the answer is not present in the information, reply exactly:

"I couldn't find that information in the college knowledge base."

---------------------------------------
College Information:
{context}
---------------------------------------

Student Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"