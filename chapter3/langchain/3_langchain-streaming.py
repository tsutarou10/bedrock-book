from bedrock_client import ChatBedrockClient
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatBedrockClient(
    streaming=True,
).client

messages = [
    SystemMessage(content="あなたのタスクはユーザの質問に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)
print("")
