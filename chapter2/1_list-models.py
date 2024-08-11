from bedrock_client import BedrockClient

bedrock = BedrockClient().bedrock
result = bedrock.list_foundation_models()

print(result)
