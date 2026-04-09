from openai import OpenAI
#1.获取client对象，创建OpenAI对象
client = OpenAI(
    base_url="https://api.deepseek.com")
#2.调用模型
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是ai助理，回答很简洁"},
        {"role": "user", "content": "小明有两条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有三条宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几只宠物"},
    ],
    stream=True#设置为True，则返回的是流式数据
)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end="",#每一段以空格分隔
          flush=True)#立即刷新缓冲区
