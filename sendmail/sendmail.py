#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import re
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import commands
import datetime


## 读取html的数据
def readHtml():
    # file_object = open('/home/wangr/python/PythonFiles/result.txt')
    file_object = open('/home/wangr/python/PythonFiles/demo1.html')
    # file_object = open('/Users/miraclewong/github/PythonBasic/sendmail/demo1.html')
    try:
        html = file_object.read()
        return html
    finally:
        file_object.close()




# 发送邮件的函数
def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


# 主程序入口
def main():
    # 发件人
    sender="report@51iwifi.com"
    # 收件人
    recevier="cfwr1991@126.com,984921316@qq.com,15381104868@189.cn"
    # date日期， title：邮件标题
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    subject = date + " Ansible配置文件仓库检查日检报告"
    html = readHtml()
    # send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", "<a href='http://www.cnblogs.com/miraclewong/'>Miracle Wong</a>")
    # send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", "Hello World")
    send_mail(sender, recevier, subject, html)

if __name__ == '__main__':
    main()
