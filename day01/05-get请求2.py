from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

args = {
    "wd":"尚学堂",
    "ie":"utf-8"
}
#拼接 地址
url="https://www.baidu.com/s?wd={}".format(urlencode(args))
# print(url)
headers ={
    "User-Agent": UserAgent().random

}
request = Request(url,headers=headers)
respponse = urlopen(request)
info = respponse.read()
print(info.decode())