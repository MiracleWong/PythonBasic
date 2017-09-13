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
from pyh import *

# aList=["1", "2", "2", "3", ["ew", "ep"]]
aList=["", "", "", ["", ""]]
# aList=["", "", "", "", ["", ""]]
# aList=["", "", "", "", ["", ""]]
d2List = []

# 日志的配置
ml = MyLog()
## 切换目录
def chdir():
    # path = "/Users/miraclewong/github/PythonBasic/Ansible"
    path = "/etc/ansible"

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
    #file_object = open('/Users/miraclewong/github/PythonBasic/PyH/result.txt')
    file_object = open('/home/wangr/python/PythonFiles/resultH.txt')
    try:
        txt = file_object.read()
        return txt
    finally:
        file_object.close()

## 读取html的数据
def readHtml():
    html_object = open('/home/wangr/python/PythonFiles/demo1.html')
    #html_object = open('/Users/miraclewong/github/PythonBasic/sendmail/demo1.html')
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


def parseTxt():
    txt = readTxt()
    host = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', txt)
    # print host
    # print "服务器的ip为: " + host[0]
    aList[0]=host[0]
    Path="/home/wangr/python/PythonFiles"
    #Path="/Users/miraclewong/github/PythonBasic/sendmail"
    os.chdir(Path)
    comm1 = "cat result.txt | grep \"^--- before:\" | awk -F ': ' '{print $2}'"
    comm2 = "cat result.txt | grep \"^--- before:\" | awk -F ': ' '{print $2}' | cut -d '/' -f 3 "
    file = commands.getoutput(comm1)  
    service = commands.getoutput(comm2)  
    # print  output
    aList[1]=service
    aList[2]=file
    # print aList[1]
    # print aList[2]
    comm3 = "cat result.txt | grep \"^-\" |grep -v \"^--- before\" "
    comm4 = "cat result.txt | grep \"^+\" |grep -v \"^+++ after\" "
    code_before = commands.getoutput(comm3)
    code_after = commands.getoutput(comm4)
    # print code_before
    # print code_after

    code_before_array = code_before.split("\n")
    # print len(code_before_array)

    code_after_array = code_after.split("\n")
    # print len(code_after_array)
    # if len(code_before_array) > len(code_before_array)
    aList[3][0] = code_before_array[0]
    aList[3][1] = code_after_array[0]
    d2List.append(aList)
    for i in range(len(code_before_array)-1):
        bList=["", "", "", ["", ""]]
        bList[3][0]=code_before_array[i+1]
        bList[3][1]=code_after_array[i+1]
        d2List.append(bList)

    # print d2List

def shellexec():
    # p = Popen(["touch HelloWorld.txt"], stdin=PIPE)
    #p = subprocess.Popen('touch HelloWorld.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen('ansible-playbook copy-templates-to-app.yml --extra-vars "hosts=172.20.3.53 app_name=devicebus-gw-5200" --check --diff > /home/wangr/python/PythonFiles/resultH.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def generateHtml():
    page = PyH('My Page')
    page<<div(style="text-align:center")<<h4('各个服务配置文件的检测')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('主机ip') + th('服务')+th('被修改文件')+th('配置项的修改前后对比')
    # print len(d2List[0][3])
    for i in range(len(d2List)):
        tr2 = mytab << tr()
        for j in range(4):
            if len(d2List[i][j])==2:
                tr2 << td('<div style="color:red">'+d2List[i][j][0]+'</div>'+'<div style="color:green">'+d2List[i][j][1]+'</div>')
            else:
                tr2 << td(d2List[i][j])
            # print d2List[i][j]
            # if list[i][j]=='192.20.3.62':
            #     tr2.attributes['bgcolor']='yellow'
            # if list[i][j]=='program1.xml':
            #     tr2[1].attributes['style']='color:red'
    #page.printOut('/Users/miraclewong/github/PythonBasic/PyH/hello.html')
    page.printOut('/home/wangr/python/PythonFiles/hello.html')


# 主程序入口
def main():

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
    chdir()
    shellexec()
    print "shellexec"
    parseTxt()
    print "parseTxt"
    generateHtml()
    print "generateHtml"
    html = readHtml()
    print "readHtml"
    send_mail(sender, recevier, subject, html)
    print "sendmail"

if __name__ == '__main__':
    main()
