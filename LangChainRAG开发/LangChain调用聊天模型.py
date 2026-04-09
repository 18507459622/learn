from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
LLM = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
#准备消息列表
messages = [
    ("system","你是一个军事家"),
    ("human","写一个计谋"),
    ("ai","苦肉计"),
    ("human","按照你上一个回复的格式，写三个计谋"),
    #AIMessage(content="锄禾热当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    #HumanMessage(content="按照你上一个回复的格式，继续写一句唐诗，四句话")
]

#调用模型流式输出
res = LLM.stream(input=messages)
for chunk in res:(
    print(chunk.content,end="",flush=True)
)