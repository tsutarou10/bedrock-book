import boto3


class BedrockClient:
    def __init__(self):
        self.my_session = boto3.Session(profile_name="default", region_name="us-east-1")
        self.bedrock = self.my_session.client("bedrock")
        self.bedrock_runtime = self.my_session.client("bedrock-runtime")
        self.anthropic_version = "bedrock-2023-05-31"
        self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
