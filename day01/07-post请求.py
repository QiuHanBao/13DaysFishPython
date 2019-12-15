from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = "http://www.sxt.cn/index/login/login.html"
form_data = {
    "user": "17703181473",
    "password": "123456"
}
headers = {
    "User-Agent": UserAgent().chrome
}
f_data = urlencode(form_data)
request = Request(url, data=f_data.encode(), headers=headers)
response = urlopen(request)
print(response.read().decode())
