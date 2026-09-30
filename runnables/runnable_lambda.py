from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)

load_dotenv()


def word_count (text):
    return len(text.split())


model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 2.0,
)

prompt_1 = PromptTemplate(
    template = "Generate a funny joke about the {topic}",
    input_variable = ["topic"],
)

parser = StrOutputParser()

generate_joke_chain = RunnableSequence(prompt_1 , model , parser)

parallee_chain = RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(generate_joke_chain ,parallee_chain )

result = final_chain.invoke({"topic":"AI"})

# final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(result)