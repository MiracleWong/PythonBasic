#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 
# 新建数据表EMPLOYEE，如果数据库crm中已经有，就先删除后建立

import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost","root","123456","crm" )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
conn.close()