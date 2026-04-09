from langchain_openai import ChatOpenAI

from langchain.schema import HumanMessage
LLM = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
res = LLM.stream(input='湖南有什么好吃的')
for chunk in res:
    print(chunk.content,end="",flush=True)