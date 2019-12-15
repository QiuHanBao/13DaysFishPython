import requests
from fake_useragent import UserAgent
from lxml import html

url = 'https://seatory.tuchong.com/12493483/#image15153135'
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
e = html.etree.HTML(response.text)
srcs = e.xpath('//article/img/@src')

print(type(srcs))
for src in srcs:
    response = requests.get(src, headers=headers)
    img_name = src[url.rfind('/') + 1:]
    with open('img/' + img_name, 'wb') as f:
        f.write(response.content)
