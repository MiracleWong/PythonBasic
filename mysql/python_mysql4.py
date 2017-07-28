#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 对数据库的查询操作
import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost","root","123456","crm" )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print "数据库中取出的数据的样式："
    print results
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
conn.close()