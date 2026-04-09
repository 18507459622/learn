from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate.from_template(
"我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答")
#调用.format 方法注入信息即可
prompt_text = prompt_template.format(lastname="张", gender="女")

llm = ChatOpenAI(model="deepseek-chat",
             base_url="https://api.deepseek.com")
# res = llm.invoke(prompt_text)
# print(res.content)
chain = prompt_template | llm
res = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res.content)