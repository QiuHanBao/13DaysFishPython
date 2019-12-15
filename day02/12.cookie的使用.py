from urllib.request import Request,urlopen
from fake_useragent import UserAgent

url=""
headers={
    "User-Agent":UserAgent().chrome,
    "Cookie":""
}

request = Request(url,headers=headers)
response=urlopen(request)
print(response.read().decode())