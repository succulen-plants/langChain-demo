import os
os.environ["SERPAPI_API_KEY"] = '8398967e3e4e20473263b8d34959480876fd618e2fd215aa6972430d03d94088'


# os.environ["OPENAI_API_BASE"] = 'https://api.chatanywhere.com.cn/v1'
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.chains.conversation.memory import ConversationBufferMemory

# OpenAI.api_base = "https://api.chatanywhere.com.cn/v1"pyt
llm = OpenAI(openai_api_key="sk-RUYMa4nzjcQHBvVmPgYvsYR3A9Nd6OwRgtK1nRqCvFfOUusn",
             openai_api_base="https://api.chatanywhere.com.cn/v1", temperature=0)
          

search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Music Search",
        func=search.run,
        # func=lambda x: "'All I Want For Christmas Is You' by Mariah Carey.", #Mock Function
        description="A Music search engine. Use this more than the normal search if the question is about Music, like 'who is the singer of yesterday?' or 'what is the most popular song in 2022?'",
    )
]

memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)
# agent.run("介绍一下CNN")

agent.run(input="hi, i am bob")
agent.run(input="what's my name?")