import streamlit as st
from bedrock_client import ChatBedrockClient
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.title("Bedrock チャット")

chat = ChatBedrockClient().client

# セッションにメッセージを定義
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="あなたのタスクはユーザの質問に明確に答えることです。"),
    ]

# メッセージを画面表示
for message in st.session_state.messages:
    if message.type != "system":
        with st.chat_message(message.type):
            st.markdown(message.content)

# チャット入力欄を定義
if prompt := st.chat_input("なんでも聞いてください"):
    # ユーザの入力をメッセージに追加
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    # モデルの呼び出しと結果の画面表示
    with st.chat_message("assistant"):
        response = st.write_stream(chat.stream(st.session_state.messages))

    # モデル呼び出し結果をメッセージに追加
    st.session_state.messages.append(AIMessage(content=response))
