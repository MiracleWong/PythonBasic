#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 
# 向数据库EMPLOYEE中插入相应的数据

import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost","root","123456","crm" )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Linux', 'Jim', 21, 'F', 5600)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()
# 关闭数据库连接
conn.close()