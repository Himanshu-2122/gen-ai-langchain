from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field


from dotenv import load_dotenv

load_dotenv()

# model = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=2,
# )

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "text-generation"
)

model = ChatHuggingFace (llm = llm)


class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age : int = Field(gt = 18 , description = "Age of the Person")
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(

    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables = ['place'],

    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | model | parser



result =  chain.invoke({"place":"India"})

print (result)


print("-----------------------------------------------------------------------------------------------")

print(type(result))


print(isinstance(result, dict))        # False
print(isinstance(result, list))        # False
print(isinstance(result, str)) 


# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field

# load_dotenv()

# # Define the model
# llm = HuggingFaceEndpoint(
#     repo_id="openai/gpt-oss-20b",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# class Person(BaseModel):

#     name: str = Field(description='Name of the person')
#     age: int = Field(gt=18, description='Age of the person')
#     city: str = Field(description='Name of the city the person belongs to')

# parser = PydanticOutputParser(pydantic_object=Person)

# template = PromptTemplate(
#     template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
#     input_variables=['place'],
#     partial_variables={'format_instruction':parser.get_format_instructions()}
# )

# chain = template | model | parser

# final_result = chain.invoke({'place':'sri lankan'})

# print(final_result)