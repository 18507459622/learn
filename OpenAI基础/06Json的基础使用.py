import json
d = {
    "name": "张三",
    "age": 18,
    "sex": "男"
}
s = json.dumps(d, ensure_ascii=False)
print(s)
l = [{
    "name": "张三",
    "age": 18,
    "sex": "男"
},
    {
    "name": "王二",
    "age": 48,
    "sex": "女"
    },
{
    "name": "妞3",
    "age": 78,
    "sex": "女"
    },
]
print(json.dumps(l, ensure_ascii=False))
json_str = '{"name": "张三", "age": 18, "sex": "男"}'
print(json.loads(json_str), type(json.loads(json_str)))
json_array_str = '[{"name": "张三", "age": 18, "sex": "男"},{"name": "王二", "age": 48, "sex": "女"},{"name": "妞3", "age": 78, "sex": "女"}]'
print(json.loads(json_array_str), type(json.loads(json_array_str)))