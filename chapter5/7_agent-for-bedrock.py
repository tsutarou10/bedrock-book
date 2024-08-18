import uuid

import boto3
import streamlit as st

agent_id = "<agent_id>"
agent_alias_id = "<agent_alias_id>"
session_id = str(uuid.uuid1())
my_session = boto3.Session(profile_name="default", region_name="us-east-1")
client = my_session.client("bedrock-agent-runtime")

st.title("Agents for Amazon Bedrock チャット")

if prompt := st.chat_input("何でも聞いてください"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = client.invoke_agent(
            inputText=prompt,
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=session_id,
            enableTrace=False,
        )

        event_stream = response["completion"]
        text = ""
        for event in event_stream:
            if "chunk" in event:
                text += event["chunk"]["bytes"].decode("utf-8")
        st.write(text)
