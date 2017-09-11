#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from pyh import *
list=[['192.20.3.58','Tomcat-data-alarm-5201','program1.xml', 'HelloWord', 'HelloPython'],['192.20.3.59','Tomcat-data-alarm-5201','program2.xml', 'HelloWord', 'HelloPython'],['192.20.3.60','Tomcat-data-alarm-5201','program3.xml', 'HelloWord', 'HelloPython'],['192.20.3.61','Tomcat-data-alarm-5201','program4.xml', 'HelloWord', 'HelloPython'],['192.20.3.62','Tomcat-data-alarm-5201','program5.xml', 'HelloWord', 'HelloPython']]
print len(list)
page = PyH('My')
page<<div(style="text-align:center")<<h4('各个服务的配置文件的检测')
mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
tr1 = mytab << tr(bgcolor="lightgrey")
tr1 << th('主机ip') + th('服务')+th('修改文件')+th('修改前内容')+th('修改后内容')
for i in range(len(list)):
    tr2 = mytab << tr()
    for j in range(5):
        tr2 << td(list[i][j])
        print list[i][j]
        if list[i][j]=='192.20.3.62':
            tr2.attributes['bgcolor']='yellow'
        if list[i][j]=='HelloWord':
            tr2[1].attributes['style']='color:red'
page.printOut('/Users/miraclewong/github/PythonBasic/PyH/demo.html')