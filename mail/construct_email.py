# -*- coding: utf-8 -*-

from email.mime.text import MIMEText

# 需要发送的文本
text = "this is a test"

# 实例化类
msg = MIMEText(text)

# 打印邮件
print "+" * 20
print msg.as_string()
print "+" * 20, "\r\n"

# 添加头
msg.add_header("From", "shiyanlou@qq.com")
# 另一种方式添加
msg['To'] = "shiyanlou@qq.com"
msg['Subject'] = "shiyanlou"

print "+" * 20
print msg.as_string()
print "+" * 20, "\r\n"
