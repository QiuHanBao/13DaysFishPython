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
# print(response.text)
e = html.etree.HTML(response.text)
# 获得每一期数据
names = e.xpath('//div/ul/li/a/b/text()')
# types = e.xpath('//div/div/ul/li/a/b/text()')
type = '4K动漫'
srcvs = e.xpath('//div/div/ul/li/a/img/@src')
srcs = e.xpath('//div/div/ul[@class="clearfix"]/li/a/@href')
baseurl = 'http://pic.netbian.com'
# 连接数据库
client = pymysql.connect(host='localhost', port=3306, user='root', password='111111', charset='utf8', db='djmysql')
cursor = client.cursor()
insql = 'insert into blog_bian  values (0,%s,%s,%s,%s)'
for name, srcv, src in zip(names, srcvs, srcs):
    print(name)
    # print(type)
    srcv = baseurl + srcv
    src = baseurl + src
    cursor.execute(insql, [type, name, srcv, src])
    client.commit()
cursor.close()
client.close()
#这是注释来测试提交到git仓库