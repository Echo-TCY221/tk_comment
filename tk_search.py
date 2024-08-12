import json
import random
import time
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 这三行代码需要放在导入execjs之前

import execjs
import urllib.parse


class Search:
    def __init__(self):
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': '__ac_nonce=066aa14b900f5c4298343; __ac_signature=_02B4Z6wo00f01uuoDygAAIDBVnjvMsKzgrbriAuAANxN9f; ttwid=1%7CcPOsOiIdIwVY7IO5ZzVGo6HqSlinLYtVNi3FgbvxwuQ%7C1722422457%7C4c469d09831c1163ed1c68c5b86e84d0b486705cbdfa26425fd51737d0fbba11; UIFID_TEMP=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b028cf66751d8a1d2389f1a729bbbd68efb644307f19cedb126f608b919dd8e4dee47e07d9720ec14d644897529013aae7; s_v_web_id=verify_lz9puxvw_Js8fdbed_eO9B_48m3_BEHV_q5agALuc6Jqv; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; dy_swidth=1536; dy_sheight=864; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; strategyABtestKey=%221722422459.222%22; csrf_session_id=c71670a2e540533432b5c58a7edb01a9; xgplayer_user_id=58293963248; fpk1=U2FsdGVkX19tXgAClolsB3vf8dgTZi6Qdy77AfYL2gpG3LGs1ByWgQwUlpU5O3rzt8NjV0WE6f00VV1bifzdjQ==; fpk2=362d7fe3d8b2581bffa359f0eeda7106; passport_csrf_token=58ca4b15f49892a28e8f8f3445a314e9; passport_csrf_token_default=58ca4b15f49892a28e8f8f3445a314e9; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; xg_device_score=7.536090283342967; UIFID=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b03bfdee60a64de863a1a6d66961bd4539f8cb0bae86aacc9930f64a02d4bce1d3df64e4540ded6a5af48ce7006d811ab4b160e487317cc151a83c22bb8b3f79db72603ef671e6df13f075f7f21aca3dc21496f3333ee430ac7839ef84c8f4da698e95f0dde30244bcd83bc7ede7fabe5e89634f58cc32255e507bebfc24f2c93b; odin_tt=38a1298354953c8e210a0dfd0e0a85cb7dec39d33d8e2165f0508a0d99970fd3c9f70598c08e4423567f98bc9a869bd0cc893a2c81edf062adde1978308def8cf2cee2ebd692d638468493edc3aefec9; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSzl6Vlh1U00rS0ZvbWIzT3BNaGxsaHU3ZXEvMWpleTVraGQ0bzRUL3ZxcjgrdkF1K0Y2MlpucVkrMS9qeDllU3pXNVFVcWI4NUZ4ZE1Bc1p1NkRUWjA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; bd_ticket_guard_client_web_domain=2; biz_trace_id=aece2d40; SEARCH_RESULT_LIST_TYPE=%22single%22; x-web-secsdk-uid=e1d4a924-c812-4fb4-ae3b-7a67c7314230; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=true',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.douyin.com/search/123?aid=ac211001-d91e-4797-a080-50692343ef94&type=general',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }

    def main(self, key_worlds, page):
        ret_data_list = []

        for i in range(0, page):
            params = {
                'device_platform': 'webapp',
                'aid': '6383',
                'channel': 'channel_pc_web',
                'search_channel': 'aweme_general',
                'enable_history': '1',
                'keyword': f'{key_worlds}',
                'search_source': 'normal_search',
                'query_correct_type': '1',
                'is_filter_search': '0',
                'from_group_id': '',
                'offset': f'{i * 15}',
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
                'msToken': 'eA1CAQZRYhptWJh5kIZ99QHw5bLa6ZsHc3R7EPz1tYxMQq-2nqdHwItvdwfTy6cV5tWlDPjtzLMUFiFf7u8vgqR8PJzBeRz1-Tnx2gGl6AbUMdg6eGWEjDSG0LMGRA==',
            }
            params_str = urllib.parse.urlencode(params)
            a_bogus = execjs.compile(open('douyin.js', encoding='utf-8').read()).call('get_a_bogus', params_str)
            params['a_bogus'] = a_bogus
            response = requests.get('https://www.douyin.com/aweme/v1/web/general/search/single/', params=params,
                                    headers=self.headers)
            # time.sleep(random.randint(3, 5))
            try:
                res = response.json()
                res_data_list = res['data']
                for res_data in res_data_list:
                    ret_data_list.append(res_data)
            except Exception as e:
                print(e)
                continue
        return ret_data_list

    def run(self, key_worlds, page):
        """关键词, 页码"""
        data = self.main(key_worlds, page)
        ret_data = {"data": data}
        return ret_data


if __name__ == '__main__':
    a = Search()
    b = a.run("生活", 3)
    print(b)
