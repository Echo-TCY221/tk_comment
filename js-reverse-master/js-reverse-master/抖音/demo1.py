import json

import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  #这三行代码需要放在导入execjs之前

import execjs
import urllib.parse
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CxuKAp-3XRMj3iwfgWy-60TlowgKidEursU3FxmGpI7w%7C1718781685%7C6f3124d912efb51fd377dcc0b1174e19b442d2b909317b34595ee926070878f2; UIFID_TEMP=29d6bea3e5a6c157a08a212e1912b5e8a78666ece26be56100fa19e58a63a45bd66a753516aef0c5c311cf327c03294c47603b66abb0f2882d3f2245d5c1eb911d5a37095aa8484e9d08de63f63162b0; s_v_web_id=verify_lxli8lyz_VMUVjReX_uX1N_4eAV_Bn5V_C6SS4eEVAOsP; xgplayer_user_id=482225988456; passport_csrf_token=50c0ba82d401af457d8e362c62a8e520; passport_csrf_token_default=50c0ba82d401af457d8e362c62a8e520; fpk1=U2FsdGVkX19vpl+gb2uECe+lwdsSQgWKHwIK8FhntZGUff79uojE134iRIuMv2fyT7K0zoUk51GgpeDVqm1V1w==; fpk2=c92baae71318dc81de51a663df2f8b4f; bd_ticket_guard_client_web_domain=2; UIFID=29d6bea3e5a6c157a08a212e1912b5e8a78666ece26be56100fa19e58a63a45b61d71e71f20b97837c257a7c7e671ad6c5d0e703fdc721a8aef667756ef4490a53b83eddde8109b3ac341a5e4be129d695bac1e40d98563ed3909993035f9e27212e949aab70d52a45388d92a6e0c14929a3fce9d12682763b8d2f2f2da7138648fe3f9bd799eea3545c41a2665120278e3406c664bb110fb09d6bf375e2fa48; dy_swidth=1536; dy_sheight=864; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; download_guide=%223%2F20240723%2F0%22; pwa2=%220%7C0%7C3%7C0%22; xgplayer_device_id=17535692635; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; d_ticket=118251b18516e43648de7d97c0d6bce8318d7; n_mh=PGv2428jvNcUM-7tF4bMcj-8UV6e-_w4golpyE7_Vc8; passport_auth_status=fe1513588b7b6c1c5080f58332a68674%2C; passport_auth_status_ss=fe1513588b7b6c1c5080f58332a68674%2C; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; publish_badge_show_info=%220%2C0%2C0%2C1721877047463%22; store-region=cn-ha; store-region-src=uid; my_rd=2; passport_assist_user=Cj10PSVwLHZm7cVazFdHmQ-XCeBaCkIfWw8dZDnFyN4lRmsiAy7N01P9JryBpErapsZSNyd1GPCLNGceJGsCGkoKPNYrxf77ncDvE0lb9ZqtaLGLDFNwyjkmVvq7CcdcF5PwDynlTRREggPdPxCC0Z6px52OUcEUABUqAMv21RDCytcNGImv1lQgASIBAyx2xMk%3D; sso_uid_tt=9b317af790e0ff44645deca052e94b23; sso_uid_tt_ss=9b317af790e0ff44645deca052e94b23; toutiao_sso_user=a4789410d54a9a33d82a797cf4ef8bb0; toutiao_sso_user_ss=a4789410d54a9a33d82a797cf4ef8bb0; sid_ucp_sso_v1=1.0.0-KGU1NWYxZDlhMGFiZjc1ODc1YjllMzU4MzFlODIzYTdiMmMzNDcyZDIKHwj1wJrmgQMQ5OGHtQYY7zEgDDCs3IDcBTgFQPsHSAYaAmxxIiBhNDc4OTQxMGQ1NGE5YTMzZDgyYTc5N2NmNGVmOGJiMA; ssid_ucp_sso_v1=1.0.0-KGU1NWYxZDlhMGFiZjc1ODc1YjllMzU4MzFlODIzYTdiMmMzNDcyZDIKHwj1wJrmgQMQ5OGHtQYY7zEgDDCs3IDcBTgFQPsHSAYaAmxxIiBhNDc4OTQxMGQ1NGE5YTMzZDgyYTc5N2NmNGVmOGJiMA; uid_tt=8c1af897dbd285870709d6e80199de7a; uid_tt_ss=8c1af897dbd285870709d6e80199de7a; sid_tt=16b0c66afd3fa7501089f4c93feb3aa1; sessionid=16b0c66afd3fa7501089f4c93feb3aa1; sessionid_ss=16b0c66afd3fa7501089f4c93feb3aa1; _bd_ticket_crypt_cookie=4704da61da18c501808696ff5d16acbc; sid_guard=16b0c66afd3fa7501089f4c93feb3aa1%7C1721889000%7C5183999%7CMon%2C+23-Sep-2024+06%3A29%3A59+GMT; sid_ucp_v1=1.0.0-KDE0NGEzYmVjZDMwYmEzYzY4MzE1ZGY2ZGE4ZDllMzcwNzM2MmUwOTAKGQj1wJrmgQMQ6OGHtQYY7zEgDDgFQPsHSAQaAmhsIiAxNmIwYzY2YWZkM2ZhNzUwMTA4OWY0YzkzZmViM2FhMQ; ssid_ucp_v1=1.0.0-KDE0NGEzYmVjZDMwYmEzYzY4MzE1ZGY2ZGE4ZDllMzcwNzM2MmUwOTAKGQj1wJrmgQMQ6OGHtQYY7zEgDDgFQPsHSAQaAmhsIiAxNmIwYzY2YWZkM2ZhNzUwMTA4OWY0YzkzZmViM2FhMQ; WallpaperGuide=%7B%22showTime%22%3A1721819803478%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A28%2C%22cursor2%22%3A0%7D; SEARCH_RESULT_LIST_TYPE=%22multi%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; strategyABtestKey=%221721959908.692%22; EnhanceDownloadGuide=%220_0_0_0_1_1721966455%22; douyin.com; xg_device_score=6.838658660324137; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; csrf_session_id=4441c59e1ae865144901a70c71514b9c; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAArABi1PkSMrJf23h7Ydcf9b5Sveo7G2AceBtYACxvlkc%2F1722009600000%2F0%2F1721973163190%2F0%22; __ac_nonce=066a35ba800da2d656e17; __ac_signature=_02B4Z6wo00f0120uFEgAAIDA0P70UXRSQDdtDhDAAL309e; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAArABi1PkSMrJf23h7Ydcf9b5Sveo7G2AceBtYACxvlkc%2F1722009600000%2F0%2F1721981864163%2F0%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUGFYOW5HalBzc0pxRmxWYTFRTCtHcWRzeEpxVGNaSjZYem5XNGVXckhoVWhKTDlaSTE1dmMvemNLTEJYSjhsUE14STVHOEtoRnFRTjNnWUpTWGRtN2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; odin_tt=1fcbf9b165387951afeaca599ed492237dd0aaeb0460b174f2d3abb92b98f0034c7b9fffb97a4fd4b5e79303eefd2f1d',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/search/%E9%A5%B0%E5%93%81?aid=bbdab962-6111-47e3-8598-a0d3e48b6c90&type=general',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'search_channel': 'aweme_general',
    'enable_history': '1',
    'keyword': '饰品',
    'search_source': 'normal_search',
    'query_correct_type': '1',
    'is_filter_search': '0',
    'from_group_id': '',
    'offset': '45',
    'count': '10',
    'need_filter_settings': '0',
    'list_type': 'multi',
    'search_id': '20240726161853A4A303128AD90101C6F6',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '190600',
    'version_name': '19.6.0',
    'cookie_enabled': 'true',
    'screen_width': '1536',
    'screen_height': '864',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '127.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '127.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '12',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7382111065314133555',
    'msToken': 'n3h56MjJSqaqfGZ12UHNcT9KfNhDSy-OEyifaaVzuWkffOEgtkO1qb5H3AHSXs19TBYMNxIVU6-p2ma-eYzmRRvWHY4dXNkkUugEDtSyBOLeCFQ5eSOmb5xf6jzrcOs=',
}


params_str = urllib.parse.urlencode(params)

a_bogus = execjs.compile(open('douyin.js', encoding='utf-8').read()).call('get_a_bogus', params_str)

print(a_bogus)
params['a_bogus'] = a_bogus
response = requests.get('https://www.douyin.com/aweme/v1/web/general/search/single/', params=params, headers=headers)

print(response.text)