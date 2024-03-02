import os
import boto3
import json
import base64
from io import BytesIO
from random import randint
from dotenv import load_dotenv

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