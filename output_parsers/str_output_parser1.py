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


# Step 1: Create first prompt
prompt_1 = template_1.invoke({"topic":"cricket"})

#tep 2: Get detailed report from LLM
result_1 = model.invoke(prompt_1)

# Step 3: Put detailed report into second prompt
prompt_2 = template_2.invoke({
    "text": result_1.content
})
# Step 4: Get summary
result_2 = model.invoke(prompt_2)

# print("DETAILED REPORT:")
# print(result_1.content)

print("\nSUMMARY:")
print(result_2.content)









print(result_1.content)

