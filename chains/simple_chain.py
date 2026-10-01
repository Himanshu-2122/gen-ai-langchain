from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


model = init_chat_model("groq:openai/gpt-oss-20b")


template = PromptTemplate(
    template = "Give the 5 key important facts about the {topic}",
    input_variables = ["topic"],
)


parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"topic":"elon must"})

print(result)

chain.get_graph().print_ascii()

