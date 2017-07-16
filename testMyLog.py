#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from myLog import MyLog


if __name__ == '__main__':
    ml = MyLog()
    ml.debug("I am the debug message")
    ml.info("I am the info message")
    ml.warn("I am the warn message")
    ml.error("I am the error message")
    ml.critical("I am the critical message")