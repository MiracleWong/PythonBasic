#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'zhangsan')   #添加
print (r.get('name'))   #获取
