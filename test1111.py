import requests
import json


headers = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImJhNjYwMzMwLWMzMzUtNGM4My1iMTQ3LTBjZjMwNjc1YWRlMSJ9.-BNZogLFeWem264L4jvMCIVuxXjVEaD4g27OvBUL2fhT5wXt1ATWVo_fkn2MHgB-myHziYT5kEZdxJ5OHhz1BA",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.265.400 QQBrowser/12.7.5768.400",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://192.168.1.14",
    "Referer": "http://192.168.1.14/ec/collectVideo",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "http://192.168.1.3:8080/letter/getOne"

response = requests.get(url, headers=headers, params={"accountId": 1}).text

dy_id_str = json.loads(response)['douYinId']
message = json.loads(response)['remarks']
dy_id_list = dy_id_str.split(',')
print(dy_id_list)
print(message)
