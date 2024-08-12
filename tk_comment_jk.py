# -*- coding: utf-8 -*-
# @Time         : 2024/7/04  18:46
# @Author       : Tang
# @ProjectName  : demo1
# @FileName     : tk_search_jk.py
# @Software     : PyCharm
"""
    Description:
"""
import json
import asyncio

import tornado.web
import tornado.ioloop  # 作用监听端口
from concurrent.futures import ThreadPoolExecutor
from tornado.options import define, options, parse_command_line
from tk_comment import Comment

Comment = Comment()


class Executor(ThreadPoolExecutor):
    """ 创建多线程的线程池，线程池的大小为10
    创建多线程时使用了单例模式，如果Executor的_instance实例已经被创建，
    则不再创建，单例模式的好处在此不做讲解
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=600)
        return cls._instance


# define 定义默认端口
# define('port', default=8899, type=int)
define('port', default=8900, type=int)


# 统一异常信息
def error_msg(req_param=''):
    error_info = {}
    error_info['error'] = '请求异常'
    error_info['error_reqParams'] = req_param
    # error_info = json.dumps([error_info, error_info], ensure_ascii=False)
    error_info = json.dumps(error_info, ensure_ascii=False)
    return error_info


# 创建请求方法
class MainHandler(tornado.web.RequestHandler):  # 继承tornado的请求手柄对象
    # executor为RequestHandler中的一个属性，在使用run_on_executor时，必须要用，不然会报错
    # executor在此设计中为设计模式中的享元模式，所有的对象共享executor的值
    executor = Executor()

    @tornado.gen.coroutine  # 异步处理 使用协程调度
    def get(self):  # get请求方法
        result = yield self._process()
        self.write(result)  # 返回响应字符串

    @tornado.concurrent.run_on_executor  # 增加并发量
    def _process(self):
        resp_str = '<h1>tornado实现获取orderbook</h1>'
        resp_str = json.dumps(resp_str, ensure_ascii=False)
        return resp_str


# bid unite
class BidUnite(tornado.web.RequestHandler):
    # executor为RequestHandler中的一个属性，在使用run_on_executor时，必须要用，不然会报错
    # executor在此设计中为设计模式中的享元模式，所有的对象共享executor的值
    executor = Executor()

    @tornado.gen.coroutine  # 异步处理 使用协程调度
    def post(self):
        # try:
        req_dict = json.loads(self.get_body_argument('local_dict'))  # 获取一个请求post参数 {local_dict:XXX}
        result = yield self._process(req_dict)
        self.write(result)
        try:
            pass
        except Exception as e:
            try:
                req_dict = self.get_body_argument('local_dict')  # 获取一个请求post参数
                error_info = error_msg(req_dict)
                self.write(error_info)
            except Exception as e:
                pass

    @tornado.concurrent.run_on_executor  # 增加并发量
    def _process(self, req_dict):
        print(req_dict)
        result = Comment.run(req_dict['aweme_id'], req_dict['page'])
        # pass
        return result


# 创建app对象 返回app应用 管理路由，指向请求方法对象  # 127.0.0.1:9900/bid_jiekou
def make_app():
    return tornado.web.Application(handlers=[
        (r'/', MainHandler),
        (r'/tk_comment', BidUnite),
    ], request_timeout=600)


async def main():
    # 解析启动命令
    parse_command_line()
    # 创建app对象
    app = make_app()
    # 监听端口给app options.port 获取启动命令的端口
    app.listen(options.port)
    # 启动
    # 监听启动的IO实例
    # tornado.ioloop.IOLoop.current().start()
    await asyncio.Event().wait()


if __name__ == '__main__':
    # # 解析启动命令
    # parse_command_line()
    # # 创建app对象
    # app = make_app()
    # # 监听端口给app options.port 获取启动命令的端口
    # app.listen(options.port)
    # # 启动
    # # 监听启动的IO实例
    # tornado.ioloop.IOLoop.current().start()
    asyncio.run(main())
