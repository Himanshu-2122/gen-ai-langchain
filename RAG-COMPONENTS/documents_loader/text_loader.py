from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


loader = TextLoader('cricket.txt' , encoding = 'utf-8')

docs = loader.load()

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 2.0,
)

prompt = PromptTemplate(
    template = "summaries this {topic}",
    input_variable = ["topic"],
)

parser = StrOutputParser()

chain = prompt | model | parser



# print(docs)

# print(type(docs))

# print(len(docs))

# print(type(docs[0]))


# print(docs[0].page_content)


# print(docs[0].metadata)

print(chain.invoke({"topic":docs[0].page_content}))