from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(
    model="deepseek-embedding",
    base_url="https://api.deepseek.com"
)
print(embeddings.embed_query("你好"))
print(embeddings.embed_documents(["你好", "世界","哈哈"]))