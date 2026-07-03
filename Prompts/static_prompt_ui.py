from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header('Reasearch Tool')
prompt = st.text_input('Enter your prompt')

if st.button('Summarize'):
    if prompt:
        response = model.invoke(prompt)
        st.write(response.content)
