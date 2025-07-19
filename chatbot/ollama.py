from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


# langsmith

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

#chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",""),
        ("user","Question:{question}")
    ]
)

# steramlit

st.title("Langchain Demo with gemma3 API")
input_text=st.text_input("Search")

#open ai LLM

llm=Ollama(model="gemma3:1b")
output_parser=StrOutputParser()

## chain

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))