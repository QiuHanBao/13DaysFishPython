from urllib.request import urlopen

url="http://www.baidu.com"
#发送请求
response=urlopen(url)
#读取内容
info=response.read()
#打印内容
#print(info.)

#打印状态码
print(response.getcode())
#答应真实url
print(response.geturl())
#打印响应头
print(response.info())