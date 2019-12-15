import requests
from fake_useragent import UserAgent
from lxml import html
import pymysql

url = 'http://datachart.500.com/ssq/'
headers = {
    'User-Agent': UserAgent().random
}
response = requests.get(url, headers=headers)
e = html.etree.HTML(response.text)
# 获得每一期数据
data_times = e.xpath('//table/tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//table/tbody[@id="tdata"]/tr[not(@class)]')
# 连接数据库
client = pymysql.connect(host='localhost', port=3306, user='root', password='111111', charset='utf8', db='djmysql')
cursor = client.cursor()
insql = 'insert into t_ball  values (0,%s,%s,%s)'
# 查看数据是否存在
select_new_data = 'select * from t_ball where data_time=%s'
data_times.reverse()
# 记录有多少条新数据
index = 0
for data in data_times:
    reslut = cursor.execute(select_new_data, [data])
    if reslut == 1:
        break
    index += 1
print(index)
# 数据反转
trs.reverse()

for i in range(index):
    red_ball = '-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    print(data_times[i] + '=redball:' + red_ball + '=blueball:' + blue_ball)
    cursor.execute(insql, [data_times[i], red_ball, blue_ball])
    client.commit()
cursor.close()
client.close()

# for time, tr in zip(data_times, trs):
#     red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
#     blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
#     print(time + '==' + red_ball + '**' + blue_ball)
#     cursor.execute(insql, [time, red_ball, blue_ball])
#     client.commit()
# cursor.close()
# client.close()
