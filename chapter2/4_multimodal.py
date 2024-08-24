import base64
import json

from bedrock_client import BedrockClient

bc = BedrockClient()
bedrock_runtime = bc.bedrock_runtime

with open("image.png", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

prompt_config = {
    "anthropic_version": bc.anthropic_version,
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "この画像は何？日本語で説明して",
                },
            ],
        },
    ],
}

body = json.dumps(prompt_config)

response = bedrock_runtime.invoke_model(
    body=body,
    modelId=bc.model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
results = response_body.get("content")[0].get("text")

print(results)
