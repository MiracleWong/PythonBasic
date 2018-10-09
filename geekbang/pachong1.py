#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request
from urllib import parse
import socket
import urllib

# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))
# try:
#     response2 = request.urlopen('http://httpbin.org/get?a=123&b=456', timeout=1)
#     print(response2.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time Out')

headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
url = 'http://httpbin.org/post'
dict = {
    "name": "value"
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, headers=headers, data=data, method='POST')
response3 = request.urlopen(req)

print(response3.read().decode('utf-8'))