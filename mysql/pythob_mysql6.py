#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 对数据库的删除操作

import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect("localhost", "root", "123456", "crm")

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL 更新语句
sql = "DELETE  FROM EMPLOYEE  WHERE AGE = '%d'" % (21)
#sql = "DELETE  FROM EMPLOYEE  WHERE AGE > '%d'" %  (21)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()

except:

   # 发生错误时进行回滚
   conn.rollback()

# 关闭数据库连接
conn.close()