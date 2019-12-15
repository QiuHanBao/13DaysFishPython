from fake_useragent import UserAgent
import requests
import json
from jsonpath import jsonpath

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    "User-Agent": UserAgent().random
}
responce = requests.get(url, headers=headers)
# 方法一
names = jsonpath(json.loads(responce.text), '$..name')
# 方法二
codes = jsonpath(responce.json(), '$..code')
print(names)
print(codes)
