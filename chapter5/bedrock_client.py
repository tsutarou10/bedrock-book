import boto3
from langchain_aws import ChatBedrock
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory


class ChatBedrockClient:
    def __init__(self, max_tokens=1000, streaming=True):
        self.client = ChatBedrock(
            model_id="anthropic.claude-3-sonnet-20240229-v1:0",
            model_kwargs={"max_tokens": max_tokens},
            credentials_profile_name="default",
            streaming=streaming,
        )


class DynamoDBChatMessageHistoryClient:
    def __init__(self, table_name, session_id):
        self.client = DynamoDBChatMessageHistory(
            table_name=table_name,
            session_id=session_id,
            boto3_session=boto3.Session(
                profile_name="default", region_name="us-east-1"
            ),
        )
