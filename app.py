import streamlit as st
from dotenv import load_dotenv
import os

import boto3
import json
import bedrock

from streamlit_carousel import carousel

st.set_page_config(layout="wide")

# st.header("BrainChip")
st.image("BrainChip logo.png", width = 200)
st.subheader("Learn Something new today!")

form = st.form(key='my_form')
topic = form.text_input(label='Topic')
level = form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
time = form.text_input(label='Time (hours)')
submit_button = form.form_submit_button(label='Submit')
notes_prompt = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Give me short notes about it."
slideshow_prompt = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Create a slideshow and present the information in bullet point form, but place an '@' character at the beginning of each slide. Provide a topic for each slide before its infortmation in CAPS LOCK. Also do not label each slide."

if submit_button:
    st.subheader("Slides")
    slideshow_output = bedrock.invoke(slideshow_prompt, 0.5, 2048)
    slides_text = slideshow_output.split("@")[2:]
    slides_dict = []
    for i in range(len(slides_text)):
        slides_dict.append(dict(title="Slide " + str(i + 1),
                                text=slides_text[i],
                                img="https://img.freepik.com/free-vector/background-realistic-abstract-technology-particle_23-2148431735.jpg"))
    carousel(items=slides_dict, height = 800)

    col1, col2, col3 = st.columns([1.425,0.15,1.425])


    with col1:
        st.subheader("Notes")
        notes = bedrock.invoke(notes_prompt, 0.5, 2048)
        st.write(notes)
        
    with col2:
        st.markdown(
    """
    <style>
    .vertical-line {
        border-left: 2px solid #808080; /* Set color and thickness of the line */
        height: 700px; /* Adjust height of the line */
        margin: auto; /* Center the line horizontally */
    }
    </style>
    <div class="vertical-line"></div>
    """,
    unsafe_allow_html=True
)
        
        


    with col3:
        st.subheader("Resources")
        # invoke_resources = f"Give a list of resources (books, videos, articles, links, etc.) for {self.topic} that are {self.level} and can be completed in {self.time} hours. For each resource, include the links (especially for websites, YouTube) if possible."
        invoke_resources = f"Provide a list of links to resources (such as books, videos, articles, etc.) for learning about {topic} at {level} level. Do not include dummy links or resources."
        resources = bedrock.invoke(invoke_resources, 0.5, 2048)
        st.write(resources)
       
