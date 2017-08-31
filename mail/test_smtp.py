# -*- coding: utf-8 -*-
# filename: utf-8

from smtplib import SMTP_SSL

client = SMTP_SSL("smtp.qq.com")

code, resp = client.login(user="shiyanlou@qq.com", password="shiyanlou")

print "是否成功登录：", resp

client.sendmail(from_addr="shiyanlou@qq.com", to_addrs="shiyanlou@qq.com", msg="Hello World")

