import os
# os.environ["OPENAI_API_KEY"] = 'sk-yWLxvXbVUqVLDW4Ff2zBbLKSTnPwngLdQdkVnY1fAy1jMWcQ'
# os.environ["OPENAI_API_KEY"] = 'sk-RUYMa4nzjcQHBvVmPgYvsYR3A9Nd6OwRgtK1nRqCvFfOUusn'
# os.environ["OPENAI_API_BASE"] = 'https://api.chatanywhere.com.cn/v1'

os.environ["SERPAPI_API_KEY"] = '8398967e3e4e20473263b8d34959480876fd618e2fd215aa6972430d03d94088'


# os.environ["OPENAI_API_BASE"] = 'https://api.chatanywhere.com.cn/v1'
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
# OpenAI.api_base = "https://api.chatanywhere.com.cn/v1"pyt
llm = OpenAI(openai_api_key="sk-RUYMa4nzjcQHBvVmPgYvsYR3A9Nd6OwRgtK1nRqCvFfOUusn",
             openai_api_base="https://api.chatanywhere.com.cn/v1")
          
chat_model = ChatOpenAI(openai_api_key="sk-RUYMa4nzjcQHBvVmPgYvsYR3A9Nd6OwRgtK1nRqCvFfOUusn",
             openai_api_base="https://api.chatanywhere.com.cn/v1")

text = "What would be a good company name for a company that makes colorful socks?"  
llm("hello")


 # 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
g = agent.run("What's the date today? What great events have taken place today in history?")
print(g)