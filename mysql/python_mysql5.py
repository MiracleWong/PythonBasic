#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 对数据库的查询操作

import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost", "root", "123456", "crm")

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()

except:
   conn.rollback()

# 关闭数据库连接
conn.close()