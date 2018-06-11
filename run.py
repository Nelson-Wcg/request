# encoding: utf-8

import requests
import settings
from wechat import Wechat

# 请求文章地址
url = "http://localhost:8087"
ret = requests.get(url)
print(ret.url)
print(ret.text)

wechat = Wechat()
wechat.request_message(ret.text)
