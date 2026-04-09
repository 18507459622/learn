from http.client import responses

from openai import OpenAI
import json
client = OpenAI(
    base_url="https://api.deepseek.com")
schema = ['日期','股票名称','开盘价','收盘价','成交量']
example_data = [
    {
        "content": "2023-01-10,股市震荡，股票强大科技今日开盘价100元人民币，一度飙升至105元，随后跌回98元人民币最终以102元人命币收盘。",
        "answers": {
                    "日期":"2023-01-10",
                    "股票名称":"强科技",
                    "开盘价":"100",
                    "收盘价":"102",
                    "成交量":"1000"}
},
    {"content": "英伟达股市利好，股票今日开盘价100元人民币，一度飙升至105元，随后跌回98元人民币最终以111元人命币收盘。",
     "answers": {"日期":"2023-01-10",
                 "股票名称":"英伟达",
                 "开盘价":"100",
                 "收盘价":"111",
                 "成交量":"8000"}
     }
]
questions =  [
    "2025-06-10， 股市利好，股票传智教育今日开盘价100元人民币，一度飙升至108元，随后跌回99元人民币最终以103元人命币收盘。",
    "2025-06-10， 股市利好，股票黑马程序员A服今日开盘价105元人民币，一度飙升至122元，随后跌回99元人民币最终以123元人命币收盘。"
]

messages = [
    {"role": "system", "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}，按JSON字符串形式输出，如果某些信息不存在，则用原文未提及代替。"}
]
for example in example_data:
    messages.append({"role": "user", "content": example["content"]})
    messages.append({"role": "assistant", "content":json.dumps( example["answers"],ensure_ascii=False)})
for q in questions:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages + [{"role": "user", "content": f"按照上述的示例请抽取这个句子的信息{q}"}]
    )
    print(response.choices[0].message.content)
