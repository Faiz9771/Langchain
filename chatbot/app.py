from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Streamlit UI
st.title("Jarvis")
input_text = st.text_input("Ask me anything:")

#prompt template
prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    ("user", "{input}"),
])

#model or llm we are using
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
output_parsers=StrOutputParser()
chain=prompt|llm|output_parsers

if input_text:
    response = chain.invoke({"input": input_text})
    st.write(response)