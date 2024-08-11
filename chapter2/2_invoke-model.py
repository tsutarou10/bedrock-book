import json
from bedrock_client import BedrockClient

bedrock_runtime = BedrockClient().bedrock_runtime

ANTHROPIC_VERSION = "bedrock-2023-05-31"
body = json.dumps(
    {
        "anthropic_version": ANTHROPIC_VERSION,
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": "Bedrock ってどういう意味？",
            },
        ],
    },
)

MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

ACCEPT = "application/json"
CONTENT_TYPE = "application/json"

response = bedrock_runtime.invoke_model(
    body=body,
    modelId=MODEL_ID,
    accept=ACCEPT,
    contentType=CONTENT_TYPE,
)
response_body = json.loads(response.get("body").read())
answer = response_body["content"][0]["text"]

print(answer)
