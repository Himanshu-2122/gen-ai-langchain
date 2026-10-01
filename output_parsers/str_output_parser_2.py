from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "text-generation"
)


model = ChatHuggingFace (llm = llm)


# prompt for detailed report
template_1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables = ['topics']
)
# prompt for summary of that detailed report 

template_2 = PromptTemplate(
    template = 'write a 5 line summary onthe following test. /n {text}',
    input_variables = ["text"]
)


parser = StrOutputParser()

chain = template_1 | model | parser | template_2 | model | parser

result = chain.invoke({"topic":"black hole"})
print(result)