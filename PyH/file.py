#!/usr/local/bin/python
# -*- coding=utf-8 -*-

txtName = "codingWord.html"
f=file(txtName, "a+")
for i in range(1,101):
    if i % 2 == 0:
        new_context = "C++" + '\n'
        f.write(new_context)
    else:
        new_context = "Python" + '\n'
        f.write(new_context)
f.close()