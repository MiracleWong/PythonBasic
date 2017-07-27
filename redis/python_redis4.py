#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import redis
pool = redis.ConnectionPool(host='192.168.0.110', port=6379)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

r.set('name', 'zhangsan')
r.set('name', 'lisi')

pipe.execute()
