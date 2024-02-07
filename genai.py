
import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key='AIzaSyDvmT5BLMRcaJxbC06GN-uHVYadO0SfU7E')
model=genai.GenerativeModel('gemini-pro')
def dnc(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Text Formation")
st.header('Application')
input=st.text_input("Input: ",key='input')
submit=st.button('Ask the question')
if submit:
  response=dnc(input)
  st.subheader("The response is:")
  st.write(response)