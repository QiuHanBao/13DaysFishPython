import requests
from fake_useragent import UserAgent
from lxml import html
import pymysql

url = 'http://pic.netbian.com/4kdongman/'
headers = {
    'User-Agent': UserAgent().random
}
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
print(response.text)
e = html.etree.HTML(response.text)
# 获得每一期数据
types = e.xpath('//div[@id="main"]/div[@class="classify clearfix"]/a/text()')
names = e.xpath('//div/div/ul/li/a/b/text()')
srcvs = e.xpath('//div/div/ul/li/a/img/@src')
srcs = e.xpath('//div/div/ul[@class="clearfix"]/li/a/@href')
baseurl = 'http://pic.netbian.com'
# 连接数据库
client = pymysql.connect(host='localhost', port=3306, user='root', password='111111', charset='utf8', db='djmysql')
cursor = client.cursor()
insql = 'insert into blog_bian  values (0,%s,%s,%s,%s)'
for type, name, srcv, src in zip(types, names, srcvs, srcs):
    srcv = baseurl + srcv
    src = baseurl + src
    cursor.execute(insql, [type, name, srcv, src])
    client.commit()
cursor.close()
client.close()
