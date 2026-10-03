from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
)

loader = PyPDFLoader("/home/himanshu/Projects/gen-ai-langchain/RAG-COMPONENTS/text-splitters/Himanshu_Vishwakarma_Resume.pdf")

docs = loader.load()

result = text_splitter.split_documents(docs)

print(result[0].page_content)
print(result)
print(len(result))