import json

import requests

# url = "https://cn-sy-bgp-plustmp1.natfrp.cloud:19754/tk_search"
# url = "http://192.168.1.7:8899/tk_search"
url = "http://192.168.1.7:8902/tk_user_video_search"

data_1 = {
    "user_sec_id": "MS4wLjABAAAAQR4WK9JBK9HPic72xsYWettM23c9_fRFjXS_4xmMKMk",
    "timestamp": 0
}

data = {
    "local_dict": json.dumps(data_1, ensure_ascii=False)
}
print(data)
response = requests.post(url, data=data, verify=False)

res_data = json.loads(response.text)['data']
for res in res_data:
    print(res)
