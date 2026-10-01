from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader 


loader = DirectoryLoader (
    "../../books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)



docs = list(loader.lazy_load())

print(docs[17].metadata)
print(docs[17].page_content)