import streamlit as st
from dotenv import load_dotenv
import os

import boto3
import json
import bedrock

from streamlit_carousel import carousel

st.header("BrainChip")
st.subheader("Learn Something new today!")

form = st.form(key='my_form')
topic = form.text_input(label='Topic')
level = form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
time = form.text_input(label='Time (hours)')
submit_button = form.form_submit_button(label='Submit')
invoke_string = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information. Give me short notes about it."

def generate_image_with_text(text, output_path='output_image.jpg'):
    # Create a blank white image
    image_width = 800
    image_height = 600
    background_color = random.choice[(255, 255, 255), (200,240,190) ]  # NEED TO CHOOSE COLOURS
    image = Image.new('RGB', (image_width, image_height), background_color)

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Set font and size (adjust as needed)
    font_path = "/Users/khushinarang/Downloads/playfair-display"  # Replace with the path to your font file
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # Set text color
    text_color = (0, 0, 0)  # Black

    # Set text position (adjust as needed)
    text_position = (50, 50)

    # Write text on the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the image
    image.save(output_path)
    
    #     AI_generated_text = ""
# we split it and then produce 
# split_slides = []

    # for (i in split_slides):
    #     generate_image_with_text(i)
    #dhhddddsb


    

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

test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        interval=None,
        img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
    ),
]

carousel(items=test_items, width=1)
    

