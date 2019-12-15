from django.test import TestCase
from urllib.request import Request
from fake_useragent import UserAgent
import requests
from fake_useragent import UserAgent
import re

# Create your tests here.

url = "http://www.lovehhy.net/Joke/Detail/QSBK/"
headers = {
    'User-Agent': UserAgent().chrome
}
# login_url = 'http:www.lanzou.com/login'
# 构造请求
response = requests.get(url, headers=headers)
info = response.text
# print(info)
# infos = re.findall(r'<div  id="endtext">\s*<br>\s*(.+)\s*<br>', info)
infos = re.findall(r'<div id="endtext">\s*(.+)<br /><br /><br /></div>', info)
print(infos)
with open('duanzi.txt', 'w', encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n\n\n")

# response = requests.post(login_url, headers=headers, data=params)
print(requests.text)
