from langchain.globals import set_debug
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

set_debug(True)

chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    credentials_profile_name="default",
)

messages = [
    SystemMessage(content="あなたのタスクはユーザの質問に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

response = chat.invoke(messages)
print(response.content)
