from langchain_huggingface import HuggingFaceEmbeddings


from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

user_query_embedding = embeddings.embed_query("who is MS dhoni")
print(user_query_embedding)

# command for install sentence_transfomer if u dont have cuda ..   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu