#!/usr/local/bin/python
'''an example for generate html page.
the module used is:PyH
Its home page is: http://code.google.com/p/pyh/
'''
from pyh import *
page = PyH('My wonderful PyH page')
page.addCSS('https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.css')
page.addJS('https://cdn.bootcss.com/jquery/1.12.4/jquery.js', 'https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.js')
page << h1('My big title', cl='center')

page << div(cl='btn btn-success', id='myDiv1') << p('I love PyH!', id='myP1')
mydiv2 = page << div(id='myDiv2')
mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
page << div(id='myDiv3')
page.myDiv3.attributes['cl'] = 'myCSSclass3'
page.myDiv3 << p('Another paragraph')
# page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
mytab = page << table(cl='table table-bordered', id='table1')
tr1 = mytab << tr(cl='active')
tr1 << td('1') + td('2')
tr2 = mytab << tr(cl='success')
tr2 << td('3') + td('4')
tr3 = mytab << tr(cl='warning')
tr3 << td('5') + td('6')
tr4 = mytab << tr(cl='danger')
tr4 << td('7') + td('8')
tr5 = mytab << tr(cl='info')
tr5 << td('9') + td('10')
page.printOut('/Users/miraclewong/github/PythonBasic/PyH/a.html')

# page = PyH('My wonderful PyH page')
# page << h2('Most compact way to build a 4 by 4 table')
# page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
# page << h2('Another way to build a 4 by 4 table')
# mytab = page << table()
# tr1 = mytab << tr()
# tr1 << td('1') + td('2')
# tr2 = mytab << tr()
# tr2 << td('3') + td('4')
# page.printOut('/Users/miraclewong/sources/table.html')