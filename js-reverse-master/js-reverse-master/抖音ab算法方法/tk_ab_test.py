import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'params': 'source_type=force&request_from=&promotion_ids=123&verifyFp=123&fp=&msToken=123%3D%3D',
    'data': '',
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'index_0': 0,
    'index_1': 1,
    'index_2': 14,
}

response = requests.post('http://39.107.101.62:8111/dy/abogus/', headers=headers, json=json_data)

print(response.text)