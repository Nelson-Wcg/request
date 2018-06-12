# encoding: utf-8
import os
from request import Request
from wechat import Wechat


请求文章地址
request = Request()
url = request.do_request()
wechat = Wechat()
wechat.request_message(url)
