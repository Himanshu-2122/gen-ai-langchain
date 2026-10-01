from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()



llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

result = llm.invoke(" who is elon musk and why he is famous ")

print(result.content)