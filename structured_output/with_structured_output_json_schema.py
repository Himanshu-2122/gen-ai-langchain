from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model="openai/gpt-oss-120b",
    temperature=1.5,
    model_provider="groq"
)

reviews_schema = {
    "title": "Reviews",
    "type": "object",
    "properties": {
        "Key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes of the reviews"
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg", "neutral"],
            "description": "Return sentiment of the review"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the pros about the review"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the cons about the review"
        },
        "name": {
            "type": "string",
            "description": "Write the reviewer name"
        }
    },
    "required": [
        "Key_themes",
        "summary",
        "sentiment",
        "pros",
        "cons",
        "name"
    ]
}

structure_model = model.with_structured_output(
    reviews_schema,
    # method="json_schema"
    # method = "function_calling"
    method="json_mode"
)

user_review = """
Waste of money

Apple wants us to fund money for Apple Duo went into research
and development. Why are people still buying new iPhones

write by shivani
"""

result = structure_model.invoke(user_review)

print(result)
print(result["sentiment"])