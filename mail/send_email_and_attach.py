# -*- coding: utf-8 -*-

from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

client = SMTP_SSL("smtp.qq.com")

client.login('shiyanlou@qq.com', 'shiyanlou')


msg = MIMEMultipart()

msg['From'] = "shiyanlou@qq.com"
msg['To'] = "shiyanlou@qq.com"
msg['Subject'] = "this is a subject"

with open("test_img.png", "rb") as f:
    img = MIMEImage(f.read(), name="test_img.png")
    msg.attach(img)

text = MIMEText("there is a img")

msg.attach(text)

client.sendmail("shiyanlou@qq.com", "shiyanlou@qq.com", msg.as_string())

client.quit()