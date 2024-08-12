import streamlit as st
from bedrock_client import ChatBedrockClient
from langchain_core.messages import HumanMessage, SystemMessage

st.title("Bedrock チャット")

chat = ChatBedrockClient().client

messages = [
    SystemMessage(content="あなたのタスクはユーザの質問に明確に答えることです"),
]

if prompt := st.chat_input("なんでも聞いてください"):  # チャット入力欄を定義
    messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):  # 引数でアバターのアイコンが変わる
        st.markdown(prompt)

    with st.chat_message("assistant"):  # モデルの呼び出しと結果の画面表示
        st.write_stream(chat.stream(messages))
