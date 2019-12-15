from urllib.request import Request,urlopen
from urllib.parse import quote

url="https://www.baidu.com/s?wd={}".format(quote("尚学堂"))

headers ={
    "User-Agent":"Mozilla"
}
request = Request(url,headers=headers)
respponse = urlopen(request)
print(respponse.read().decode())
