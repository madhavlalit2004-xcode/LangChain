from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r'C:\Users\sodiu\OneDrive\Documents\Coding\LangChain\testing',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)