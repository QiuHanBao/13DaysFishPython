import requests
from fake_useragent import UserAgent

session = requests.Session()
headers = {
    "User-Agent": UserAgent().chrome
}
login_url = "http://www.sxt.cn/index/login/login"
params = {
    "user": "177031814873",
    "password": "12356"
}
respone = session.post(login_url, headers=headers, data=params)
info_url = "http://www.sxt.cn/index/user.html"
resp = session.get(info_url, headers=headers)
print(resp.text)
