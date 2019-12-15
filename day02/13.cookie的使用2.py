from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor,build_opener
#登录
login_url="http://www.sxt.cn/index/login/login"
headers={
    "User-Agent":UserAgent().chrome
}
form_data={
    "user":"17703181473",
    "password":"12345"
}
f_data=urlencode(form_data).encode()
request = Request(login_url,headers=headers)
# response=urlopen(request) 错误的
handler= HTTPCookieProcessor()
opener=build_opener(handler)
response=opener.open(request)
# print(response.read().decode())

#f访问页面
info_url="http://www.sxt.cn/index/user.html"
request=Request(info_url,headers=headers)
# response=urlopen(request)
response=opener.open(request)
print(response.read().decode())