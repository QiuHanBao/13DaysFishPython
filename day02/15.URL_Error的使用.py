from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.error import URLError


url = ''
headers ={
    "User-Agent":UserAgent().chrome
}

try:
    req=Request(url,headers=headers)
    resp=urlopen(req)
    print(resp.read().decode())
except URLError as e:
    print(e)
print("访问完成")
