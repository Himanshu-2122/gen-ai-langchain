from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from typing import TypedDict , Annotated , Optional

load_dotenv()


model = init_chat_model(
    model="openai/gpt-oss-120b",
    temperature=1.5,
    model_provider="groq"
)

# schema 
class Reviews(TypedDict):
    Key_themes : Annotated[list[str] ,"write dowm all the key theme of the reviews" ]
    summary: Annotated[str , "A Brief summary of the my reviews"]
    sentiment: Annotated[str , "Return sentiment of the review in following format of (neutral , negative , positive)"]
    pros : Annotated[Optional[list[str]] ,"write down all the pros about the reviews" ]
    cons : Annotated[Optional[list[str]] ,"write down all the cons about the reviews" ]
    name : Annotated[Optional[str], "write the reviewer name"]

structure_model = model.with_structured_output(
    Reviews,
    method="json_schema"
)


user_review = """
Waste of money

Apple wants us to fund money for Apple Duo went into research
and development. Why are people still buying new iPhones

write by shivani
"""


result = structure_model.invoke(user_review)

print(result)

print(result["name"])