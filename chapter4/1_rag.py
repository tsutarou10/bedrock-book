import streamlit as st
from bedrock_client import ChatBedrockClient
from langchain_aws import ChatBedrock
from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="SMABQ7MN5V",
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
    region_name="us-east-1",
    credentials_profile_name="default",
)

prompt = ChatPromptTemplate.from_template(
    "以下のcontext に基づいて回答してください: {context} / 質問: {question}",
)
model = ChatBedrockClient(streaming=False).client

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

st.title("おしえて！Bedrock")
question = st.text_input("質問を入力")
button = st.button("質問する")

if button:
    st.write(chain.invoke(question))
