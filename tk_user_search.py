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
            'cookie': 'ttwid=1%7CcPOsOiIdIwVY7IO5ZzVGo6HqSlinLYtVNi3FgbvxwuQ%7C1722422457%7C4c469d09831c1163ed1c68c5b86e84d0b486705cbdfa26425fd51737d0fbba11; UIFID_TEMP=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b028cf66751d8a1d2389f1a729bbbd68efb644307f19cedb126f608b919dd8e4dee47e07d9720ec14d644897529013aae7; s_v_web_id=verify_lz9puxvw_Js8fdbed_eO9B_48m3_BEHV_q5agALuc6Jqv; dy_swidth=1536; dy_sheight=864; xgplayer_user_id=58293963248; fpk1=U2FsdGVkX19tXgAClolsB3vf8dgTZi6Qdy77AfYL2gpG3LGs1ByWgQwUlpU5O3rzt8NjV0WE6f00VV1bifzdjQ==; fpk2=362d7fe3d8b2581bffa359f0eeda7106; passport_csrf_token=58ca4b15f49892a28e8f8f3445a314e9; passport_csrf_token_default=58ca4b15f49892a28e8f8f3445a314e9; UIFID=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b03bfdee60a64de863a1a6d66961bd4539f8cb0bae86aacc9930f64a02d4bce1d3df64e4540ded6a5af48ce7006d811ab4b160e487317cc151a83c22bb8b3f79db72603ef671e6df13f075f7f21aca3dc21496f3333ee430ac7839ef84c8f4da698e95f0dde30244bcd83bc7ede7fabe5e89634f58cc32255e507bebfc24f2c93b; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; is_staff_user=false; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; store-region=cn-zj; store-region-src=uid; MONITOR_WEB_ID=b9097cce-762c-4675-a870-310f17504f87; my_rd=2; passport_mfa_token=Cjd%2BH5uPydFfnvwcp6%2BTnKu9HsFQJma4gFgYeHxiWdwlTnWAec5IYA663HxY3d4BYvPO7hesfwByGkoKPJsddY%2BqIwFx0aqnE8Q%2FPMWZQwPMcWYGuQdUXnTB1sR%2FI1gr07FMTS5CeqIaPwkWX8pzLVjmLvWIMEfiohDQtNgNGPax0WwgAiIBA15nIqg%3D; d_ticket=53806980efff5b863511ca1ec579a162153e7; passport_assist_user=CkFzjB2Sr6bLtCxetLQQzQRGMCu2DRAcyH5-g_JdXwQWFm8dJGS9AAEAh_6V5Le_xdZRmorttkmcuwFdMcXXxcqGoRpKCjwJWPfmcbP-YmxnnHxKtG-NSeC2-fGaKkGGyB7jqHnkswU6m1naFPGta46Lza39NpHrz10IU0MIni1Z8jsQ7LLYDRiJr9ZUIAEiAQOYYNtJ; n_mh=6YBN04s1dkH3XeC5bIOI2kb_srLW1SSL76Y19gAeUK0; sso_uid_tt=9f351be2a96b70a60adddd25bd1323ad; sso_uid_tt_ss=9f351be2a96b70a60adddd25bd1323ad; toutiao_sso_user=926799147e972179a800fe5f789b9936; toutiao_sso_user_ss=926799147e972179a800fe5f789b9936; sid_ucp_sso_v1=1.0.0-KDU3YzExNjk4YzFmMGU1YTE1MDVjNGYzMDUwNzUwZmRlMzQ4ZjBhNjIKIQiuipD0__STBRD47bi1BhjvMSAMMN7R__sFOAZA9AdIBhoCbHEiIDkyNjc5OTE0N2U5NzIxNzlhODAwZmU1Zjc4OWI5OTM2; ssid_ucp_sso_v1=1.0.0-KDU3YzExNjk4YzFmMGU1YTE1MDVjNGYzMDUwNzUwZmRlMzQ4ZjBhNjIKIQiuipD0__STBRD47bi1BhjvMSAMMN7R__sFOAZA9AdIBhoCbHEiIDkyNjc5OTE0N2U5NzIxNzlhODAwZmU1Zjc4OWI5OTM2; passport_auth_status=04e7fcfbbe43dd5a8af80316ba3efa1a%2Cc07c690870bfef052466163f30a65c9d; passport_auth_status_ss=04e7fcfbbe43dd5a8af80316ba3efa1a%2Cc07c690870bfef052466163f30a65c9d; uid_tt=822288638a192fa76f682bfa5c5a8fef; uid_tt_ss=822288638a192fa76f682bfa5c5a8fef; sid_tt=e363d80abed35a1c3418f305afabbd97; sessionid=e363d80abed35a1c3418f305afabbd97; sessionid_ss=e363d80abed35a1c3418f305afabbd97; _bd_ticket_crypt_cookie=3cea47acdbe1f77f5aab3e0a300387b7; sid_guard=e363d80abed35a1c3418f305afabbd97%7C1722693373%7C5183998%7CWed%2C+02-Oct-2024+13%3A56%3A11+GMT; sid_ucp_v1=1.0.0-KGE1YmU3M2E1MTM5ZjQzYjAxMGIxOGYyNGNhOGIzMzU1NGE3MDAyNTAKGwiuipD0__STBRD97bi1BhjvMSAMOAZA9AdIBBoCbGYiIGUzNjNkODBhYmVkMzVhMWMzNDE4ZjMwNWFmYWJiZDk3; ssid_ucp_v1=1.0.0-KGE1YmU3M2E1MTM5ZjQzYjAxMGIxOGYyNGNhOGIzMzU1NGE3MDAyNTAKGwiuipD0__STBRD97bi1BhjvMSAMOAZA9AdIBBoCbGYiIGUzNjNkODBhYmVkMzVhMWMzNDE4ZjMwNWFmYWJiZDk3; download_guide=%223%2F20240801%2F1%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=066b995ff0022846ef6a7; __ac_signature=_02B4Z6wo00f01rTOENwAAIDBCR7wxNakkfq07hRAAMuWbd; douyin.com; xg_device_score=7.496591075245761; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; csrf_session_id=7dcfbeaa8f88d4588cc57567c8054792; strategyABtestKey=%221723438596.87%22; biz_trace_id=6b38fcda; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; passport_fe_beating_status=true; WallpaperGuide=%7B%22showTime%22%3A1722496067942%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A63%2C%22cursor2%22%3A0%2C%22hoverTime%22%3A1722497862295%7D; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; publish_badge_show_info=%220%2C0%2C0%2C1723438952668%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSzl6Vlh1U00rS0ZvbWIzT3BNaGxsaHU3ZXEvMWpleTVraGQ0bzRUL3ZxcjgrdkF1K0Y2MlpucVkrMS9qeDllU3pXNVFVcWI4NUZ4ZE1Bc1p1NkRUWjA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=0d8660f05896af48f0c2d16b2442b9f98036ba75998ec46739bf26e9fd32ad48cd942937fd298726f51c0bbdf4a083f3',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.douyin.com/search/%E5%B0%8F%E5%85%9C%E5%AE%9D?type=user',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }

    def main(self, key_worlds):
        ret_data_list = []

        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'search_channel': 'aweme_user_web',
            'keyword': f'{key_worlds}',
            'search_source': 'normal_search',
            'query_correct_type': '1',
            'is_filter_search': '0',
            'from_group_id': '',
            'offset': '0',
            'count': '20',
            'need_filter_settings': '1',
            'list_type': 'single',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'version_code': '170400',
            'version_name': '17.4.0',
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
            'webid': '7397748033510901259',
            'msToken': '-_izTO7EpNNamWfu036gamFprBCigz5xD1d2Z4oSEgsBKjuYJYTv2s4tj7OifK0UgQdKKWCNSQtKyR-MSmLmX7XTYaf66PP9cX8ShYFp8fjaUkZL64rmTv8uuelxO0s=',
        }
        params_str = urllib.parse.urlencode(params)
        a_bogus = execjs.compile(open('douyin.js', encoding='utf-8').read()).call('get_a_bogus', params_str)
        params['a_bogus'] = a_bogus
        response = requests.get('https://www.douyin.com/aweme/v1/web/discover/search/', params=params,
                                headers=self.headers)
        time.sleep(random.randint(3, 5))
        try:
            res = response.json()
            res_data_list = res['user_list']
            for res_data in res_data_list:
                ret_data_list.append(res_data)
        except Exception as e:
            print(e)

        return ret_data_list

    def run(self, key_worlds):
        """关键词, 页码"""
        data = self.main(key_worlds)
        ret_data = {"data": data}
        return ret_data


if __name__ == '__main__':
    a = Search()
    b = a.run("小兜宝")
    for i in b['data']:
        print(i)
    print(len(b['data']))
