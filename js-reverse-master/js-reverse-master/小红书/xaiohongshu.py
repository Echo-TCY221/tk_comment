import json
import pprint
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests

cookies = {
    'abRequestId': '9b3394c75ed1f55b32dd0ac922329caf',
    'a1': '18e6edbfbcedkrnytmr4c77yv6tgtqvz2c5d61lou50000370066',
    'webId': '62aa25ae3dc2d4af0b841afc212af1dd',
    'gid': 'yYdKdfDiY0J4yYdKdfDiDSy1SdfTFIv96F4S2l7WWvhK9f28k9AhuK888qW88KK8dWiWd0i4',
    'web_session': '040069b48bf60e0e8d27b1a3b2344b0ed49da0',
    'customer-sso-sid': '68c51738813529448782544289a1217c90eb7b48',
    'x-user-id-creator.xiaohongshu.com': '65ffb546000000001700dd71',
    'customerClientId': '604216648355517',
    'access-token-creator.xiaohongshu.com': 'customer.creator.AT-68c517390323262497525804hrixfcduyoivqgmh',
    'xsecappid': 'xhs-pc-web',
    'acw_tc': '6649695453e8af106d2f461f268fc441b085d4de252269982f29f1db9d2bcafe',
    'webBuild': '4.27.7',
    'websectiga': 'f47eda31ec99545da40c2f731f0630efd2b0959e1dd10d5fedac3dce0bd1e04d',
    'sec_poison_id': 'd95b4421-0243-47e6-a6f6-c452786a4a47',
    'unread': '{%22ub%22:%226695e3e600000000030270e9%22%2C%22ue%22:%22669026480000000003026be0%22%2C%22uc%22:15}',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'abRequestId=9b3394c75ed1f55b32dd0ac922329caf; a1=18e6edbfbcedkrnytmr4c77yv6tgtqvz2c5d61lou50000370066; webId=62aa25ae3dc2d4af0b841afc212af1dd; gid=yYdKdfDiY0J4yYdKdfDiDSy1SdfTFIv96F4S2l7WWvhK9f28k9AhuK888qW88KK8dWiWd0i4; web_session=040069b48bf60e0e8d27b1a3b2344b0ed49da0; customer-sso-sid=68c51738813529448782544289a1217c90eb7b48; x-user-id-creator.xiaohongshu.com=65ffb546000000001700dd71; customerClientId=604216648355517; access-token-creator.xiaohongshu.com=customer.creator.AT-68c517390323262497525804hrixfcduyoivqgmh; xsecappid=xhs-pc-web; acw_tc=6649695453e8af106d2f461f268fc441b085d4de252269982f29f1db9d2bcafe; webBuild=4.27.7; websectiga=f47eda31ec99545da40c2f731f0630efd2b0959e1dd10d5fedac3dce0bd1e04d; sec_poison_id=d95b4421-0243-47e6-a6f6-c452786a4a47; unread={%22ub%22:%226695e3e600000000030270e9%22%2C%22ue%22:%22669026480000000003026be0%22%2C%22uc%22:15}',
    'origin': 'https://www.xiaohongshu.com',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-b3-traceid': '16b5c812ab8e7863',
    # 'x-s': 'XYW_eyJzaWduU3ZuIjoiNTIiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjU4NTUxZWRmNzZlMTYyODlkYzU3ZmIyN2MxNjQ3NGZhNTc5Yzk4NTBmMTlhZjU0MmZhNzFkOGQ3YmM4ZDM4NTU3YzU2MjJiY2U0YTUwMWMyZDZkYmNkMTBhZmI5NTU2MGQwNTc1MDMwNTY2NTA0MjE4ODgxNDNkOWFkNGRkYmQ5ODg4MTQzZDlhZDRkZGJkOWI1NmNjM2EzN2M2YTdhYWRlOTM2NTBhZGMzMzlkZTY0MGQwNzFlMjA5ZjczODE2MTU4MThiMzcyNGUwNmI2MzNhYmMwYWVjMDYxYWZlMDA5NWM5ZmQ1ZDY5ZDU5MmRiYTJlYTQ5NzBmMGE1MzRiZmE3ZGJiZTVmNmFiNGIyNjFiNDViMzg0MzNkOTdjNzNiMzBjNWQ3NDE2ZTY2YmMzNzJlY2IwZWQzMDk1NjE5NDc4N2M1ZTNjMjFkNjA5N2RiZjMzNzk3NTI1N2ZmYzc3NGIxZjQ0ZWJhMDA2NmFiMTBhYTJkNDEzM2RkNGJjNzhiOSJ9',
    'x-s-common': '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',
    # 'x-t': '1722305158598',
}

# 路径
c = '/api/sns/web/v1/homefeed'
json_data = {
    'cursor_score': '',
    'num': 31,
    'refresh_type': 1,
    'note_index': 35,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed_recommend',
    'search_key': '',
    'need_num': 6,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': False,
}
data = json.dumps(json_data, separators=(',', ':'))
print(data)
params = execjs.compile(open('xhs.js', 'r', encoding='utf-8').read()).call('get_x_s', c, json_data)
print(params)
headers['x-s'] = params['X-s']
headers['x-t'] = str(params['X-t'])   # 生成的时间戳是int类型,需要转化为字符串类型
response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                         data=data)
print(response.text)
