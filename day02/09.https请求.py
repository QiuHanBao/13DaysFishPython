from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl

url ='https://www.12306.cn/mormhweb/'
headers ={
    "User-Agent":UserAgent().chrome
}

request=Request(url,headers=headers)
#忽略证书
context=ssl._create_unverified_context()
response=urlopen(request,context=context)
info=response.read().decode()
print(info)