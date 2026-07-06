from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text_generation"
)

model = ChatHuggingFace(llm=llm)

#Prompt 1 - detailed prompt
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#Prompt 2 - summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'Black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.content)