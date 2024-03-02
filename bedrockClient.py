from dotenv import load_dotenv
from dotenv import load_dotenv
import os
import boto3
import json

class BedrockClient:
    def __init__(self):
        load_dotenv(".env")
        self.bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=os.environ.get('AWS_DEFAULT_REGION'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.environ.get('AWS_SESSION_TOKEN')
        )

    def invoke(self, prompt, temperature, max_tokens):
        """
        Invoke the Bedrock model with the given prompt and return the response.
        Args:
            prompt (str): The prompt to send to the model.
            temperature (float): The tone used to answer.
            max_tokens (int): The maximum number of characters to output.
        """
        prompt_config = {
            "prompt": f'\n\nHuman: {prompt} \n\nAssistant:',
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature
        }

        response = self.bedrock_runtime.invoke_model(
            body=json.dumps(prompt_config),
            modelId="anthropic.claude-v2"
        )

        response_body = json.loads(response.get("body").read())

        return response_body.get("completion")