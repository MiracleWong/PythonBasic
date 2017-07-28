#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 
# 测试是否成功连接MySQL数据库

import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost","root","123456","crm" )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
conn.close()