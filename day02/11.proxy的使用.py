from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = 'http://httpbin.org/get'
headers = {
    "User-Agent": UserAgent().chrome
}

request = Request(url, headers=headers)
# 有密码的使用方法
# handler=ProxyHandler({"http":"username:password@ip:port"})
# handler=proxyHandler({"http":})
# 无密码的使用方式
# handler = ProxyHandler({"http":"ip:port"})
handler = ProxyHandler({"http":"118.190.95.43:9001"})
opener=build_opener(handler)
response=opener.open(request)
print(response.read().decode())