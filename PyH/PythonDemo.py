#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import sys
import os
import re
from myLog import MyLog
# def execAnsible():
#     status = os.system('sh ~/svnrepos/1.sh')




ml = MyLog()
host = []
serviceName = ""
modifyFiles = ""
modifyContentBefore = ""
modifyContentAfter = ""

content_before ='+<Server port="5211" shutdown="SHUTDOWN"> + <Connector port="5201" protocol="HTTP/1.1" + <Connector port="5221" protocol="AJP/1.3" redirectPort="8443" />'

content_after ='-<Server port="5210" shutdown="SHUTDOWN"> - <Connector port="5200" protocol="HTTP/1.1" - <Connector port="5220" protocol="AJP/1.3" redirectPort="8443" />'
def getPath():
    pass

## 切换目录
def chdir():
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
    

## 读取TXT的数据
def readTxT():
    file_object = open('/Users/miraclewong/PythonFiles/result5.txt')
    try:
        str = file_object.read()
        # print str
    finally:
        file_object.close()
        # print str

    # host = re.findall(r'\-.*', str)
    # print host
    # print "服务器的ip为: " + host[0]
    # ll_r=re.compile(r'^\-.*')
    # print ll_r.search(str)
    
    # ml.debug("服务器的ip为:" + host[0])
    # str.search(ll_r)
    # print type(l)
    # ml.debug("lll:" + l[0])

    # m = re.match(r'^-', str)
    # if m:
    #     print m.group(0)
    # else:
    #     pass

    # code_before_array = content_before.split("+")
    # for modify_code_before in code_before_array:
    #     ml.debug("修改前的代码为:" + modify_code_before.strip())
    # code_after_array = content_after.split("-")
    # for modify_code_after in code_after_array:
    #     ml.debug("修改后的代码为:"+ modify_code_after.strip())


    aList = ['', '', '', '', '', ['', '']]
    # ml.debug("lll:" + aList)

def writeContent():
    pass

def main():
    readTxT()


if __name__ == '__main__':
    main()