from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from fake_useragent import UserAgent
from urllib.parse import urlencode

#登录
#保存cookie到文件中
login_url="http://www.sxt.cn/index/login/login"
headers={
    "User-Agent":UserAgent().chrome
}
form_data={
    "user":"17703181473",
    "password":"12345"
}