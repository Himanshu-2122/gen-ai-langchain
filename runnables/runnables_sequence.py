# #text = "Innovation shapes our modern world in ways previously unimaginable, bridging distant cultures and transforming daily routines. Technology acts as a catalyst, accelerating progress across education, healthcare, and industry while presenting new ethical challenges. As we navigate this digital frontier, maintaining our humanity, empathy, and critical thinking remains vital. True advancement measures its success not merely by efficiency or speed, but by how sustainably it improves quality of life for every individual globally. Embracing these opportunities requires courage, collaboration, and a relentless commitment to building a more inclusive, balanced, and harmonious future for coming generations everywhere."
# # text = "Innovation shapes our modern world in ways previously unimaginable, bridging distant cultures and transforming daily routines. Technology acts as a powerful catalyst, accelerating progress across education, healthcare, and industry while presenting new ethical challenges. As we navigate this complex digital frontier, maintaining our shared humanity, empathy, and critical thinking remains vital. True advancement measures its success not merely by efficiency or speed, but by how sustainably it improves quality of life for every individual globally. Embracing these opportunities requires courage, collaboration, and a relentless commitment to building a more inclusive, balanced, and harmonious future for coming generations everywhere."

# text = "Innovation shapes our modern world in ways previously unimaginable, bridging distant cultures and transforming daily routines. Technology acts as a powerful catalyst, accelerating progress across education, healthcare, and industry while presenting new ethical challenges. As we navigate this complex digital frontier, maintaining our shared humanity, empathy, and critical thinking remains vital. True advancement measures its success not merely by efficiency or speed, but by how sustainably it a improves quality of life for every individual globally. Embracing these opportunities requires courage, collaboration, and a relentless commitment to building a more inclusive, balanced, and harmonious future for coming generations everywhere today."
# def word_count (text):
#     return len(text.split())


# res = word_count(text)

# print(res)


from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
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

seq_chain = prompt_1 | model | parser | prompt_2 | model | parser

print(seq_chain.invoke({"topic":"RUSSIA VS INDIA"}))