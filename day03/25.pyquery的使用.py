from pyquery import PyQuery
from fake_useragent import UserAgent
import requests

url = "https://www.xicidaili.com/nn/"
headers = {
    'User-Agent': UserAgent().random
}
response = requests.get(url, headers=headers)
doc = PyQuery(response.text)
trs = doc('#ip_list tr')  # 获得所有的td  ip列表
# 通过循环获得所有的ip
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    types = trs.eq(num).find('td').eq(5).text()
    print(ip + ':' + port + "------" + types)
