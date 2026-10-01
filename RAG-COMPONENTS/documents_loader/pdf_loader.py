from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("gen-ai-book.pdf")

docs = loader.load()



print(docs[10].page_content)

print(docs[10].metadata)