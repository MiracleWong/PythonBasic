#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# 首先定义一个RedisHelper类，连接Redis，
# 定义频道为monitor，定义发布(publish)及订阅(subscribe)方法。


import redis

class RedisHelper(object):
    """docstring for RedisHelper"""
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1', port=6379) #连接Redis
        self.channel = 'monitor'  # 定义名称
        
    # 定义发布方法
    def publish(self, msg):
        self.__conn.publish(self.channel, msg)
        return True

    # 定义订阅方法
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub
        return True