#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from pyh import *

page = PyH('My wonderful PyH page')
mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
for i in range(5):
    mytr = mytab << tr()
    for j in range(5):
        mytr << td('Row %s, column %s' % (i, j))
page.printOut('/Users/miraclewong/github/PythonBasic/PyH/table.html')