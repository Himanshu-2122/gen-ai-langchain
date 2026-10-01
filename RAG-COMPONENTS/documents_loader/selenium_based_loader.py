from langchain_community.document_loaders import SeleniumURLLoader
urls = ["https://www.instagram.com/"]

loader = SeleniumURLLoader (urls = urls , browser = "firefox" , headless = True)

docs = loader.load()

print("Total documents:", len(docs))


for doc in docs:
    print("\nSOURCE:", doc.metadata.get("source"))
    print("TITLE :", doc.metadata.get("title"))
    print("TEXT  :", doc.page_content[1])