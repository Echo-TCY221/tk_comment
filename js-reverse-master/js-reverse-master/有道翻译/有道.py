import json
import pprint
import re
import requests
import time
import hashlib
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
timestamp = str(int(time.time() * 1000))
# print(timestamp)
sign_text = "client=fanyideskweb&mysticTime={}&product=webfanyi&key=fsdsogkndfokasodnaso".format(timestamp)
# print(sign_text)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1697782891.6805668; OUTFOX_SEARCH_USER_ID=444444444@127.0.0.1'
}

while True:
    try:
        word = input("请输入你要翻译的中文内容(输入0即可退出):\n")
        if word == '0':
            print('已退出翻译系统')
            break
        words = re.sub("\s", "", word)
        data = {
            'i': words,
            'from': 'auto',
            'to': '',
            'dictResult': 'true',
            'keyid': 'webfanyi',
            'sign': hashlib.md5(sign_text.encode()).hexdigest(),
            'client': 'fanyideskweb',
            'product': 'webfanyi',
            'appVersion': '1.0.0',
            'vendor': 'web',
            'pointParam': 'client,mysticTime,product',
            'mysticTime': timestamp,
            'keyfrom': 'fanyi.web',
        }

        response = requests.post('https://dict.youdao.com/webtranslate', headers=headers, data=data)
        t = response.text
        # print('响应为:', t)
        # data = execjs.compile(jsCode).call('get_data', t)
        node_command = ['node', 'youdao.js', t]
        data = subprocess.run(node_command, capture_output=True, text=True, check=True)
        # print("data:", data)
        result = subprocess.run(node_command, capture_output=True, text=True, check=True)
        json_data = json.loads(result.stdout)
        # pprint.pprint(json_data)
        result = json_data['translateResult'][0][0]['tgt']
        if json_data.get('dictResult') != -1:
            tran = json_data['dictResult']['ce']['word']['trs'][0]['#tran']
        print('翻译结果为:', result + '\n译义:\n' + tran)
    except Exception as e:
        print('翻译失败,输入内容不合法')
