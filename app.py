import streamlit as st
from dotenv import load_dotenv
import os

import boto3
import json
import bedrock

st.header("BrainChip")
st.subheader("Learn Something new today!")

form = st.form(key='my_form')
topic = form.text_input(label='Topic')
level = form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
time = form.text_input(label='Time (hours)')
submit_button = form.form_submit_button(label='Submit')
invoke_string = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Give me short notes about it."

if submit_button:
    col1, col2 = st.columns([2, 3.5])


    with col1:
        st.subheader("Notes")
        notes = bedrock.invoke(invoke_string, 0.5, 2048)
        st.write(notes)
        
        st.subheader("Suggestions")


    with col2:
        st.subheader("Slides")
        
        st.subheader("Chatbot")


    

