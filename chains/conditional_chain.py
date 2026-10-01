from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model_1 = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq",
)

model_2 = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google_genai",   # fixed: underscore, not hyphen
)

str_parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Give the sentiment of the following feedback"
    )


py_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction': py_parser.get_format_instructions()}
)

classifier_chain = prompt_1 | model_1 | py_parser

prompt_2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt_3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt_2 | model_1 | str_parser),
    (lambda x: x.sentiment == "negative", prompt_3 | model_2 | str_parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

# classifier_chain PEHLE chalao, uska output branch_chain ko do
final_chain = classifier_chain | branch_chain

result = final_chain.invoke({"feedback": "this is a sexy looking phone"})

print(result)

final_chain.get_graph().print_ascii()