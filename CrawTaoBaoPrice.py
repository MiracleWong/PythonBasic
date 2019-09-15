#!/usr/bin/python
# -*- coding:utf8 -*-

import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 获取HTML Text


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except Exception as e:
        raise e


def printGoodsList(ilt):
    tplt = "{:4}\t{:10}\t{:16}"
    print(tplt.format("排序", "商品价格", "商品名称"))
    count = 0

    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

# 主函数


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except Exception as e:
            raise e
    printGoodsList(infoList)
    # url = 'http://www.xlpu.cc/html/45875.html'
    # html = getHTMLText(url)
    # print html


# 程序总入口
if __name__ == '__main__':
    main()
