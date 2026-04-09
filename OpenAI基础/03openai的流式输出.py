from openai import OpenAI
#1.获取client对象，创建OpenAI对象
client = OpenAI(
    base_url="https://api.deepseek.com")
#2.调用模型
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家"},
        {"role": "assistant", "content": "好的我是一个编程专家，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用Python代码"},
    ],
    stream=True#设置为True，则返回的是流式数据
)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end="",#每一段以空格分隔
          flush=True)#立即刷新缓冲区
