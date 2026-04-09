from langchain_openai import ChatOpenAI
'''统一对话消息模式'''
from langchain.schema import HumanMessage
'''初始化模型'''
LLM = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
messages = [HumanMessage(content="你好，用LangChain调用DeepSeek模型")]
response = LLM.invoke(messages)
print(response.content)