import requests
from fake_useragent import UserAgent

headers ={
    "User-Agent":UserAgent().chrome
}
login_url="http://www.sxt.cn/index/login/login"
params ={
    "user":"177031814873",
    "password":"12356"
}
respone =requests.post(login_url,headers=headers,data=params)
print(respone.text)