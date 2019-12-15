from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import html
import requests

url = 'https://www.qidian.com/rank?chn=21'
ua = UserAgent().random
uachrome = UserAgent().chrome

headers = {
    "User-Agent": uachrome
}
responce = requests.get(url, headers=headers)
# e = html.etree(responce.text)
e = html.etree.HTML(responce.text)
names = e.xpath('//h4/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')

for name, author in zip(names, authors):
    print(name + ":" + author)
