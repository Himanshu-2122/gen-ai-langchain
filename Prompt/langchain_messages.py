from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.5
)


messages = [
        SystemMessage(content='You are helpful assistant'),
        HumanMessage(content="Tell me about about langchain")
]

result = model.invoke(messages)
content = result.content
if isinstance(content, list):
    text = "\n".join(
        item["text"]
        for item in content
        if item.get("type")=="text"
    )
else :
    text = content



messages.append(AIMessage(content=text))

print(messages)

 
