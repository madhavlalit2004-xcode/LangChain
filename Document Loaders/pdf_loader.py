from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\sodiu\OneDrive\Documents\Coding\LangChain\testing\financial_sectors.pdf')

docs = loader.load()

print(len(docs))