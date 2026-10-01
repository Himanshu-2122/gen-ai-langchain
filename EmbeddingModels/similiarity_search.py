from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Documents
documents = [
    "India is a country in South Asia.",
    "India has a large and diverse population.",
    "Python is a popular programming language.",
]

# Query
query = "Tell me about Python"

# Create embedding for query
query_embedding = embeddings.embed_query(query)

# Create embeddings for documents
document_embeddings = embeddings.embed_documents(documents)

# Calculate cosine similarity
similarity_scores = cosine_similarity(
    [query_embedding],
    document_embeddings
)[0]

# Get index and score of the most similar document
index, score = max(
    enumerate(similarity_scores),
    key=lambda x: x[1]
)

print("Most similar document:")
print(documents[index])

print("\nSimilarity score:", score)