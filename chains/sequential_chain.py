from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core .prompts import PromptTemplate
from dotenv import load_dotenv


# laod env 
load_dotenv()

# defining model 

model = init_chat_model("groq:openai/gpt-oss-20b")

# declaring the prompt tamplate 

template_1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables = ['topic']
)

template_2 =  PromptTemplate(
    template="From this report:\n{text}\nGive 5 most important points.",
    input_variables = ['text']
)

# defining the parser

parser = StrOutputParser()

# creating the chain for squential chain excution
chain = template_1 | model | parser | template_2 | model | parser

# invoking the chain

result = chain.invoke({"topic":"AI"})

# printing the result 

print (result)

# look how our chain looks like 

chain.get_graph().print_ascii()


