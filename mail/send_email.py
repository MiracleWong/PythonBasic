# -*- coding: utf-8 -*-

from smtplib import SMTP_SSL
from email.mime.text import MIMEText

client = SMTP_SSL("smtp.qq.com")

# 此处替换成自己的 qq 邮箱账户和授权码
client.login('shiyanlou@qq.com', 'shiyanlou')

text = "this is a test"

msg = MIMEText(text)

# 添加相应的字段值，需修改为自己的对应邮箱
msg['From'] = "shiyanlou@qq.com"
msg['To'] = "shiyanlou@qq.com"
msg['Subject'] = "this is a subject"

# 在发送邮件时，发送的应该是字符串，所以，此处使用 msg.as_string(),记得修改相应的地址
client.sendmail(from_addr="shiyanlou@qq.com", to_addrs=["shiyanlou@qq.com"], msg=msg.as_string())