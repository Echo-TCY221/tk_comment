import json

import requests

url = "https://cn-sy-bgp-plustmp1.natfrp.cloud:19754/tk_search"
# url = "http://192.168.1.7:8899/tk_search"
# url = "http://127.0.0.1:8901/tk_user_search"

data_1 = {
    "key_worlds": "小兜包",
    "page": 3
}

data = {
    "local_dict": json.dumps(data_1, ensure_ascii=False)
}

response = requests.post(url, data=data, verify=False)

res_data = json.loads(response.text)['data']
for res in res_data:
    print(res)
