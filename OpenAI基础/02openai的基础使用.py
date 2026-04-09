from openai import OpenAI
#1.获取client对象，创建OpenAI对象
client = OpenAI(
    base_url="https://api.deepseek.com")
#2.调用模型
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且不说废话"},
        {"role": "assistant", "content": "好的我是一个编程专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用Python代码"},
    ]
)
#3.查看结果
print(response.choices[0].message.content)
