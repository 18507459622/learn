from openai import OpenAI
from pyexpat.errors import messages

client = OpenAI(
    base_url="https://api.deepseek.com")
example_data = {
    '新闻报道':'今日，股市经历了一波震荡，股票价格Changed significantly.',
    '财务报告':'本公司年度财务报告显示，收入Changed significantly.',
    '公司报告':'本公司宣布成功完成最新一轮并购交易',
    '分析师报告':'最新的行业分析报告指出，公司Changed significantly.'
}

example_types = ['新闻报道', '财务报告', '公司报告', '分析师报告']

questions = [
    " 今日，央行发布公告宣布降低利率，来刺激经济增长",
    "abc公司宣称已完成对zxc公司的股权收购交易",
    "公司的资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资交易提供了坚实的财务基础",
    " 最新的报告分析指出，可再生能源行业预计在未来几年经历持续增长，投资者应该关注这一领域的投资机会",
    "小明喜欢小红"
]

messages = [
    {"role": "system", "content": "你是一个金融专家，你需要根据提供的文本内容，判断该文本内容属于哪种类型，将文本按照['新闻报道','财务报告','公司公告','分析师报告'],不清楚的分类为不清楚类别"}
]
for key, value in example_data.items():
     messages.append({"role": "user", "content": value})
     messages.append({"role": "assistant", "content": key})
#向模型提问
for q in questions:
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages + [{"role": "user", "content": f"按照实例回答这段文本的分类类别：{q}"}],
)
    print(response.choices[0].message.content)