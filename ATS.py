import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pdf2image,io,base64

genai.configure(api_key='AIzaSyDvmT5BLMRcaJxbC06GN-uHVYadO0SfU7E')
model=genai.GenerativeModel('gemini-pro')


def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content(input,pdf_content,prompt)
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        
    ## convert pdf to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        
        first_page=images[0]
        
        img_byte_arr=io.BytesIO()
        first_page.save(img_byte_arr,format=='JPEG')
        img_byte_arr=img_byte_arr.getvalue()
        
        pdf_parts=[
            {
                "mime_type":"image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        
        return pdf_parts
    else:
        
        raise FileNotFoundError('No file Uploaded')
    
    
st.set_page_config(page_title="ATS Tracking")
st.header('ATS Tracker')
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader('Upload the resume(PDF)..',type=["pdf"])

if uploaded_file is not None:
    st.write('PDF Uploaded')
    
    
submit1=st.button("Resume Summary")
submit2=st.button("Ways to improvise")
submit3=st.button("Match Percentage")

input_prompt1="""
    You are expert Human Resource Manager with full knowledge of every job, 
    your task is to review the provided resume against the job description
    pls share the professional evaluation of the resume on whether the resume aligns with the job description
    Highlight important points from the resume, also its weakness and strength points in relation to the job description
"""

input_prompt2="""
    You are expert HR manager with full knowledge of every job,
    your task is to improvise the resume according to the job description.
    Highlight skills, experience, keywords and another areas where the resume can be improved and what are the major missing points.
"""

input_prompt3="""
    You are expert HR manager with full knowledge of every job and expert in Application tracking system and knows about every functionality of deep ATS,
    your task is to evaluate the resume with respect to the job description.
    Give me the percentage match and what can improve the score.
    If the score is below 70 than create a sample resume that perfectly aligns with the job 
    description and as well the uploaded resume.
    if the score is above 70 then say the resume is fine and only the important keywords that should be added can be shown
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader('The Response is')
        st.write(response)
    else:
        st.write('Pls upload the pdf')
        
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader('The Response is')
        st.write(response)
    else:
        st.write('Pls upload the pdf')
        
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader('The Response is')
        st.write(response)
    else:
        st.write('Pls upload the pdf')