#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    # print('Run child process %s (%s)...' % (name, os.getpid()))
    print('Run child process %s (%s)...parent\'s id is (%s)' %
          (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')