import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key='AIzaSyDvmT5BLMRcaJxbC06GN-uHVYadO0SfU7E')
from youtube_transcript_api import YouTubeTranscriptApi

def extract_text(Youtube_video_url):
    try:
        video_id=Youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript=""
        for i in transcript_text:
            transcript+=" "+i["text"]
        
        return transcript
            
    except Exception as e:
        raise e
    
    
prompt="""
    You are a Youtube Video Summarizer. Using the trancript text try to 
    summarize the whoe youtube video in 300 words in bullet points
    Pls provide the summary of text:
    
"""


def generate_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text


st.title('Youtube Summarizer')
link=st.text_input('Enter the link')
if link:
    video_id=link.split("=")[1]
    print(video_id) 
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
    
if st.button('Get Detailed Notes'):
    transcript_text=extract_text(link)
    if transcript_text:
        summary=generate_content(transcript_text,prompt)
        st.markdown("## Notes:")
        st.write(summary)
     