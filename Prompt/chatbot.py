from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.5
)

chat_history = [
    SystemMessage(content="You are helpful AI assistant")
]

while True:

    user_input = input("You: ")

    if user_input == "exit":
        break

    if not user_input.strip():
        continue

    # 1. Add user's message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # 2. Send complete history to model
    result = model.invoke(chat_history)

    # 3. Get model response
    content = result.content

    if isinstance(content, list):
        text = "\n".join(
            item["text"]
            for item in content
            if item.get("type") == "text"
        )
    else:
        text = content

    # 4. Display response
    print("AI:", text)

    # 5. Add AI response to history
    chat_history.append(
        AIMessage(content=text)
    )

print(chat_history)