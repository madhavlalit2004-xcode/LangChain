from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

def word_count(text):
    return len(text.split())

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_cahin = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count': RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_cahin)
result = final_chain.invoke({'topic': 'AI'})
print(result)