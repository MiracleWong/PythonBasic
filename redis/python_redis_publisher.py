#!/usr/local/bin/python
# -*- coding:utf-8 -*-

# 订阅
from RedisHelper import RedisHelper

obj = RedisHelper()
obj.publish('nihao')#发布
