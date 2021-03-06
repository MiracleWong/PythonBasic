#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import getpass
import sys


class MyLog(object):

    """这个类用于创建一个自定义的log"""
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logfile = sys.argv[0][0:-3] + '.log' #日志文件名
        print(logfile)
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        '''日志显示到屏幕上并输出到日志文件内'''
        loghand = logging.FileHandler(logfile)
        loghand.setFormatter(formatter)
        loghand.setLevel(logging.ERROR)  # 只有错误才会被记录到日志中
        loghandst = logging.StreamHandler()
        loghandst.setFormatter(formatter)

        self.logger.addHandler(loghand)
        self.logger.addHandler(loghandst)
    
    '''日志的5个级别，对应以下的5个函数'''
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug(" I'm debug ")
    mylog.info(" I'm info ")
    mylog.warn(" I'm warn ")
    mylog.error(" I'm error ")
    mylog.critical(" I'm critical ")
