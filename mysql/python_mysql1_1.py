#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 测试是否成功连接MySQL数据库，每隔3秒中检查一次

import time
import MySQLdb

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

second = sleeptime(0,0,3)

# 打开数据库连接
conn = MySQLdb.connect("localhost","root","123456","crm" )
while 1==1:
    print "do action"
    # 使用cursor()方法获取操作游标 
    cursor = conn.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()

    print "Database version : %s " % data
    time.sleep(second)


# 关闭数据库连接
conn.close()