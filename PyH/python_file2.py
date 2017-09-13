#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from pyh import *
list=[['192.20.3.58','Tomcat-data-alarm-5201','program1.xml', ['Hello Word Hello Word Hello Word', 'Hello  Python Hello Python Hello Python']],['','','program2.xml', ['HelloWord', 'HelloPython']],['','','program3.xml', ['HelloWord', 'HelloPython']],['192.20.3.61','Tomcat-data-alarm-5201','program4.xml', ['HelloWord', 'HelloPython']],['192.20.3.62','Tomcat-data-alarm-5201','program5.xml', ['HelloWord', 'HelloPython']]]
print len(list)
page = PyH('My')
page<<div(style="text-align:center")<<h4('各个服务的配置文件的检测')
mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
tr1 = mytab << tr(bgcolor="lightgrey")
tr1 << th('主机ip') + th('服务')+th('被修改文件')+th('配置项的修改前后对比')
print len(list[0][3])
for i in range(len(list)):
    tr2 = mytab << tr()
    for j in range(4):
        if len(list[i][j])==2:
            tr2 << td('<div style="color:red">'+list[i][j][0]+'</div>'+'<div style="color:green">'+list[i][j][1]+'</div>')
        else:
            tr2 << td(list[i][j])
        # print list[i][j]
        # if list[i][j]=='192.20.3.62':
        #     tr2.attributes['bgcolor']='yellow'
        # if list[i][j]=='program1.xml':
        #     tr2[1].attributes['style']='color:red'
page.printOut('/Users/miraclewong/github/PythonBasic/PyH/hello.html')
# page.printOut('/Users/miraclewong/github/PythonBasic/PyH/demo.html')