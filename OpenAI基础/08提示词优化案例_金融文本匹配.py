from openai import OpenAI
client = OpenAI(
    base_url="https://api.deepseek.com")
example_data = {
    "是":[
    ("公司abc发布了季度财报，显示盈利增长。","财报披露，公司abc利润上升"),
    ("公司ac在2023年4月19日发布财报，显示盈利增长。","财报披露，公司ac更赚钱了")
],
    "不是": [
        ("黄金价格下跌，投资者抛售","外汇市场交易额创下新高"),
        ("央行降息，刺激经济增长","新能源技术的创新")
    ]
}

questions = [
    ("利润上升，影响房地产市场。","高利润对房地产有一定冲击"),
    ("油价大幅下跌，能源公司面临挑战。","未来城市建设趋势越加明显"),
    ("股票市场今日大涨，投资者乐观。","持续上涨的股票让投资者满意")
]

messages = [
    {"role": "system", "content": f"你帮我完成信息抽匹配，我给你2个句子,被[]包围，你判断他们是否匹配回答是或者不是，请参考如下示例。"}
]
for key,value in example_data.items():
    for v in value:
        messages.append({"role": "user", "content":f"句子1:[{v[0]}],句子2:[{v[1]}]"})
        messages.append({"role": "assistant", "content": key})
for q in questions:
    response =client.chat.completions.create(
        model="deepseek-chat",
        messages=messages + [{"role": "user", "content": f"请判断句子1:[{q[0]}],句子2:[{q[1]}]是否匹配。"}]
    )
    print(response.choices[0].message.content)