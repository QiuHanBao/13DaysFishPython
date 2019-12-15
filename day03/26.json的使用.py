import json

str = '{"name":"Hello,树先生"}'
# 字符串转字典类型
obj = json.loads(str)
dic = json.loads(str)
a = type(obj)
print(a)

# 字典转成字符串
bj = json.dumps(obj, ensure_ascii=False)
dump = type(bj)
print(dump, ":", bj)

# 序列化为 文件
# --------以utf-8的格式写入 并且 把 使用ascii 关闭   默认为 True    
json.dump(dic, open('movie.txt', 'w', encoding='utf-8'), ensure_ascii=False)
