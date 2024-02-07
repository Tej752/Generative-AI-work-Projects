
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key='AIzaSyDvmT5BLMRcaJxbC06GN-uHVYadO0SfU7E')
model=genai.GenerativeModel('gemini-pro-vision')
def Definition(input_prompt,image):
    response=model.generate_content([input_prompt,image[0]])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
            "mime_type":uploaded_file.type,
            "data":bytes_data
            }
        ]
        
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
     
    





st.set_page_config(page_title="Calories")
st.header('Cal Application')
uploaded_file=st.file_uploader('Choose an image..',type=(["jpeg","png","jpg"]))
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)
    
    

submit=st.button("Tell the Total Calories")

input_prompt="""
    Your are a nutrition expert. By looking the image uploaded provide the calories details of each item in the image.
    the format followed should be 
    1 Item Name: No. of Calories
    
    2 Item Name: No of Calories
    
    --------------
    
    -------------
    
    Also explain the food is good for health or not. Thereby explaining all the variants like Carbohydrate, Protein, Fats, Sugars in percentage.
    
    Also provide the alternative for the food displayed if unhealthy else give food contents are good.
    
    Provide the alternative as if the image displayed shows vegetarian food then vegetarian else non-veg

"""







if submit:
    image_data=input_image_setup(uploaded_file)
    response=Definition(input_prompt,image_data)
    st.header("The response is:")
    st.write(response)