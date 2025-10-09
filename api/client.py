import requests
import streamlit as st

#creating a function to get the response calling the endpoint
def get_response(topic):
    response = requests.post(
        "http://localhost:8000/topic/invoke",
        json={"input": {"topic": topic}}
    )
    
    return response.json()["output"]["content"]

#creating a streamlit app
st.title("Jarvis")
input_text = st.text_input("Shoot any topic:")

if input_text:
    response = get_response(input_text)
    st.write(response)