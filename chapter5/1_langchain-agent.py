import nest_asyncio
import streamlit as st
from bedrock_client import ChatBedrockClient
from bs4 import BeautifulSoup
from langchain import hub as prompts
from langchain.agents import AgentExecutor, Tool, create_xml_agent
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, SystemMessage

nest_asyncio.apply()


def web_page_reader(url: str) -> str:
    loader = WebBaseLoader(url)
    content = loader.load()[0].page_content
    return content


# 検索ツールと Web ページ読み込みツールの設定
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="このツールはユーザから検索キーワードを受け取り、Web上の最新情報を検索します。",
    ),
    Tool(
        name="WebBaseLoader",
        func=web_page_reader,
        description="このツールはユーザからURL を渡された場合に内容をテキストで返却します。URLの文字列のみを受け付けます。",
    ),
]

chat = ChatBedrockClient(max_tokens=1500, streaming=False).client

agent = create_xml_agent(chat, tools, prompt=prompts.pull("hwchase17/xml-agent-convo"))

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
)

st.title("Bedrock Agent チャット")
messages = [SystemMessage(content="あなたは質問に対して必ず日本語で回答します。")]

prompt = st.chat_input("何でも聞いてください。")
if prompt:
    messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        result = agent_executor.invoke({"input": prompt})
        st.write(result["output"])
