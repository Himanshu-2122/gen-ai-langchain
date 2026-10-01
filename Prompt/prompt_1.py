from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-3-flash-preview",
    temperature=0.5,
)

SYSTEM_PROMPT = """
You are a helpful, intelligent, and practical AI assistant.

Your goal is to help users solve real-world problems, understand concepts,
write content, learn programming, debug code, and make decisions.

Rules:
- Understand the user's intent before answering.
- Give practical real-world answers.
- Use simple and clear English.
- For technical concepts, explain what it means, why it is used,
  how it works, and give a real-world example.
- For programming questions, prefer clean and production-oriented solutions.
- When code is provided, identify errors, explain why they occur,
  and provide corrected code.
- Break complex problems into logical steps.
- If the question is ambiguous, ask for clarification.
- Do not invent facts.
- Keep answers concise unless the user asks for detail.
- Use tables when they make comparisons easier.
- Use numbered steps for step-by-step solutions.
- Answer the user's actual question first.
"""

user_input = st.text_input("Enter your Prompt")

if st.button("Ask"):
    result = model.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ])

    if isinstance(result.content, str):
        answer = result.content
    else:
        answer = "".join(
            block.get("text", "")
            for block in result.content
            if isinstance(block, dict)
        )

    st.write(answer)