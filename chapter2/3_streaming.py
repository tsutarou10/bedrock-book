import json
from bedrock_client import BedrockClient

bc = BedrockClient()
bedrock_runtime = bc.bedrock_runtime

body = json.dumps(
    {
        "anthropic_version": bc.anthropic_version,
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "いろは歌をおしえて",
                    },
                ],
            },
        ],
    },
)

response = bedrock_runtime.invoke_model_with_response_stream(
    body=body, modelId=bc.model_id
)
for event in response.get("body"):
    chunk = json.loads(event["chunk"]["bytes"])
    if (
        chunk["type"] == "content_block_delta"
        and chunk["delta"]["type"] == "text_delta"
    ):
        print(chunk["delta"]["text"], end="")

print()
