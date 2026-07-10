from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\sodiu\OneDrive\Documents\Coding\LangChain\testing\financial_sectors.pdf')

docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = "\n"
)

result = splitter.split_documents(docs)

print(result)