from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=2.0)

prompt_1 = PromptTemplate(
    template="Write a detailed report about {topic}",
    input_variables=["topic"],  # Note: corrected input_variable -> input_variables
)

prompt_2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

# 1. First, define the report generation chain
report_gen_chain = RunnableSequence(prompt_1, model, parser)

# 2. Define the branch that checks word count on the generated text string
summarization_branch = RunnableBranch(
    (
        lambda x: len(x.split()) > 300,
        RunnableSequence(prompt_2, model, parser),
    ),
    RunnablePassthrough(),
)

# 3. Combine them: Generate the report first, then pass it to the branch
final_chain = RunnableSequence(report_gen_chain, summarization_branch)

result = final_chain.invoke({"topic": "Russia and Ukraine"})

print(result)