from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "http://www.baidu.com"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"]
headers = {
    "User-Agent": choice(user_agents)
}

request = Request(url, headers=headers)
# print(request.get_header("User-agent"))
response = urlopen(request)

info = response.read()

print(info.decode())
