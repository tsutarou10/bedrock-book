import streamlit as st
from bedrock_client import ChatBedrockClient, DynamoDBChatMessageHistoryClient
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

st.title("Bedrock チャット")

if "session_id" not in st.session_state:
    st.session_state.session_id = "session_id"

if "history" not in st.session_state:
    st.session_state.history = DynamoDBChatMessageHistoryClient(
        table_name="BedrockChatSessionTable",
        session_id=st.session_state.session_id,
    ).client

if "chain" not in st.session_state:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたのタスクはユーザの質問に明確に答えることです。"),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="human_message"),
        ]
    )

    chat = ChatBedrockClient().client

    chain = prompt | chat
    st.session_state.chain = chain

if st.button("履歴クリア"):
    st.session_state.history.clear()

for message in st.session_state.history.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

if prompt := st.chat_input("何でも聞いてください。"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(
            st.session_state.chain.stream(
                {
                    "messages": st.session_state.history.messages,
                    "human_message": [HumanMessage(content=prompt)],
                },
                config={"configurable": {"session_id": st.session_state.session_id}},
            ),
        )
    st.session_state.history.add_user_message(prompt)
    st.session_state.history.add_ai_message(response)
