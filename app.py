import streamlit as st
from dotenv import load_dotenv
import os

import boto3
import json

load_dotenv(".env")

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.environ.get('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.environ.get('AWS_SESSION_TOKEN')
)

def invoke(prompt, temperature, max_tokens):
    prompt_config = {
        "prompt": f'\n\nHuman: {prompt} \n\nAssistant:',
        "max_tokens_to_sample": max_tokens,
        "temperature": temperature
    }

    response = bedrock_runtime.invoke_model(
        body=json.dumps(prompt_config),
        modelId="anthropic.claude-v2"
    )

    response_body = json.loads(response.get("body").read())

    return response_body.get("completion")

if st.button("test", type="primary"):
    result = invoke("hello", 0.5, 2048)
    st.write('result: %s' % result)
    
form = st.form(key='my_form')
topic = form.text_input(label='Topic')
level = form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
time = form.text_input(label='Time (hours)')
submit_button = form.form_submit_button(label='Submit')
invoke_string = "I want to learn about" + topic + "and I have" + time + "hours. I am looking for " + level + "information."

if submit_button:
    result = invoke(invoke_string, 0.5, 2048)
    st.write('result: %s' % result)