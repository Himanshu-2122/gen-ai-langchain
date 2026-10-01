import streamlit as st
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from langchain_core.prompts import PromptTemplate

from prompt_generator import template
from langchain_core.prompts.loading import load_prompt

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# model = ChatOllama(
#     model = "deepseek-r1:1.5b",
#     base_url = "http://localhost:11434"
# )


# st.header("Research Tool")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.5,
)


# model = init_chat_model(
#     model = "deepseek-r1:1.5b",
#     base_url = "http://localhost:11434",
#     model_provider = "ollama",
# )




paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

# fill the placehoder



if st.button("Ask"):
    with st.spinner("Thinking.."):

        chain = template | model

        result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input,
        })

        
        content = result.content

        if isinstance(content, list):
            text = "\n".join(
            item["text"]
            for item in content
            if item.get("type") == "text"
        )
        else:
            text = content

    st.markdown(text)




# with st.form("research_form"):
    
#     user_input = st.text_input("Enter your prompt")
#     submitted = st.form_submit_button("Ask")

#     if submitted and user_input:

#         result = model.invoke(user_input)
#         st.write(result.content)

