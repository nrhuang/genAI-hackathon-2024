import streamlit as st
from dotenv import load_dotenv
import os

import boto3
import json
import bedrock

from streamlit_carousel import carousel

st.set_page_config(layout="wide")

st.header("BrainChip")
st.subheader("Learn Something new today!")

form = st.form(key='my_form')
topic = form.text_input(label='Topic')
level = form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
time = form.text_input(label='Time (hours)')
submit_button = form.form_submit_button(label='Submit')
notes_prompt = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Give me short notes about it."
slideshow_prompt = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Create a slideshow with bullet points, but place an '@' character at the beginning of each slide. Also do not label each slide, limit each slide to 250 characters, and create at least 3 slides."

if submit_button:
    col1, col2 = st.columns([2, 3.5])


    with col1:
        st.subheader("Notes")
        notes = bedrock.invoke(notes_prompt, 0.5, 2048)
        st.write(notes)
        
        st.subheader("Suggestions")


    with col2:
        st.subheader("Slides")
        slideshow_output = bedrock.invoke(slideshow_prompt, 0.5, 2048)
        slides_text = slideshow_output.split("@")[2:]
        slides_dict = []
        for i in range(len(slides_text)):
            slides_dict.append(dict(title="Slide " + str(i + 1),
                                    text=slides_text[i],
                                    img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4"))
        carousel(items=slides_dict, width=1)
        st.subheader("Chatbot")

    

