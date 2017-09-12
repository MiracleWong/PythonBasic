#!/usr/local/bin/python
# -*- coding: utf-8 -*-

__doc__ = """The sendMail.py is to generate the reports of the config files which had been modified in the online services of the servers。This file use the PyH module to convert the text to the html.
"""
__author__ = "Wang Rui"
__version__ = 'v0.1.0'
__date__ = '2017-09-09'

import argparse
import sys
import os
import re
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import subprocess
import commands
import datetime
from myLog import MyLog
import commands

aList=["", "", "", "", ["", ""]]
aList[0]="Hello"
d2List = [];

# 日志的配置
ml = MyLog()
## 切换目录
def chdir():
    path = "/Users/miraclewong/github/PythonBasic/Ansible"
    # path = "/etc/ansible"

    # 查看当前工作目录
    retval = os.getcwd()
    # print "当前工作目录为 %s" % retval
    ml.debug("当前工作目录为: " + retval)

    # 修改当前工作目录
    os.chdir(path)

    # 查看修改后的工作目录
    retval = os.getcwd()
    # print "目录修改成功 %s" % retval
    ml.debug("目录修改成功: " + retval)

# 读取txt文本数据
def readTxt():
    file_object = open('/Users/miraclewong/github/PythonBasic/PyH/result.txt')
    # file_object = open('/home/wangr/python/PythonFiles/resultH.txt')
    try:
        txt = file_object.read()
        return txt
    finally:
        file_object.close()

## 读取html的数据
def readHtml():
    # file_object = open('/home/wangr/python/PythonFiles/demo1.html')
    html_object = open('/Users/miraclewong/github/PythonBasic/sendmail/demo1.html')
    try:
        html = html_object.read()
        return html
    finally:
        html_object.close()

# 发送邮件的函数
def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


output = commands.getstatusoutput('ls')  
print  output 
def parseTxt():
    txt = readTxt()
    # print txt
    host = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', txt)
    print host
    print "服务器的ip为: " + host[0]
    aList[0]=host[0]
    aList[1]=

def shellexec():
    # p = Popen(["touch HelloWorld.txt"], stdin=PIPE)
    p = subprocess.Popen('touch HelloWorld.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p = subprocess.Popen('ansible-playbook copy-templates-to-app.yml --extra-vars "hosts=172.20.3.53 app_name=devicebus-gw-5200" --check --diff > /home/wangr/python/PythonFiles/resultH.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# 主程序入口
def main():
    # 日志的配置

    # 发件人
    sender="report@51iwifi.com"
    # 收件人
    recevier="cfwr1991@126.com,984921316@qq.com,15381104868@189.cn"
    # date日期， title：邮件标题
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    subject = date + " Ansible配置文件仓库检查日检报表"
    # html = readHtml()
    # send_mail(sender, recevier, subject, html)
    # txt = readTxt()
    # print txt
    # chdir()
    # shellexec()
    # txt = readTxt()
    # print txt
    # print aList[0]
    parseTxt()

if __name__ == '__main__':
    main()
