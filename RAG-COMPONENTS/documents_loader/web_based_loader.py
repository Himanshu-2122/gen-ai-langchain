from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://news.ycombinator.com",
]

loader = WebBaseLoader(urls)
docs = loader.load()

print("Total documents:", len(docs))
for doc in docs:
    print("\nSOURCE:", doc.metadata.get("source"))
    print("TITLE :", doc.metadata.get("title"))
    print("TEXT  :", doc.page_content[:300])