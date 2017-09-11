#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from pyh import *

page = PyH('My wonderful PyH page')
page << h2('Most compact way to build a 4 by 4 table')
page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
page << h2('Another way to build a 4 by 4 table')
mytab = page << table()
tr1 = mytab << tr()
tr1 << td('1') + td('2')
tr2 = mytab << tr()
tr2 << td('3') + td('4')
page.printOut('/Users/miraclewong/github/PythonBasic/PyH/table.html')