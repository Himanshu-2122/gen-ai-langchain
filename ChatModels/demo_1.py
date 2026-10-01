# from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0.9,
#     # max_tokens=100,
# )

# result = model.invoke("Write something about India.")

# print(result.content)

# model = ChatGoogleGenerativeAI(
#     model = "models/gemini-3-flash-preview",
#     temperature = 0,
# )

# result =  model.invoke("write something about america ")

# print(result.content)


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("who is M.S.Dhoni")

print(result.content)