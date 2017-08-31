# -*- coding: utf-8 -*-

from smtplib import SMTP_SSL 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

client = SMTP_SSL("smtp.qq.com")
# 此处填写自己的邮箱账号和授权码，
client.login('shiyanlou@qq.com', 'shiyanlou')

# 打开图片文件
with open("test_img.png", "rb") as f:
    img = MIMEImage(f.read(), name="test_img.png")
    img.add_header("Content-ID", "img_id")

msg = MIMEMultipart()

html = MIMEText("""
<p> there is a img </p>
<img src="cid:img_id">
""", "html", "utf-8")

msg.attach(img)
msg.attach(html)

msg['From'] = "shiyanlou@qq.com"
msg['To'] = "shiyanlou@qq.com"
msg['Subject'] = "this is a subject"

client.sendmail("shiyanlou@qq.com", "shiyanlou@qq.com", msg.as_string())

client.quit()