#!/usr/local/bin/python
'''an example for generate html page.
the module used is:PyH
Its home page is: http://code.google.com/p/pyh/
'''
from pyh import *
# page = PyH('My wonderful PyH page')
# page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
# page.addJS('myJavascript1.js', 'myJavascript2.js')
# page << h1('My big title', cl='center')
# page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
# mydiv2 = page << div(id='myDiv2')
# mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
# page << div(id='myDiv3')
# page.myDiv3.attributes['cl'] = 'myCSSclass3'
# page.myDiv3 << p('Another paragraph')
# page.printOut('/Users/miraclewong/sources/a.html')

page = PyH('My wonderful PyH page')
page << h2('Most compact way to build a 4 by 4 table')
page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
page << h2('Another way to build a 4 by 4 table')
mytab = page << table()
tr1 = mytab << tr()
tr1 << td('1') + td('2')
tr2 = mytab << tr()
tr2 << td('3') + td('4')
page.printOut('/Users/miraclewong/sources/table.html')