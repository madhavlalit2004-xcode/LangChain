from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/s?k=laptop+of&adgrpid=1321614581893400&hvadid=82601169602102&hvbmt=bp&hvdev=c&hvlocphy=260581&hvnetw=o&hvqmt=p&hvtargid=kwd-82601789197989%3Aloc-90&hydadcr=3785_1993867&mcid=9ad7cf590bb23e6aacf7a6961582929c&msclkid=82b33527ff281099239c5f6830568949&tag=msndeskstdin-21&ref=pd_sl_6r92clczyv_p'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'What is the product that we are talking about', 'text': docs[0].page_content})
print(result)