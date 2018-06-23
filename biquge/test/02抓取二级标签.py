#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/6/6 14:21
@Author  : Fate
@File    : 02抓取二级标签.py
'''

import requests

import lxml
from lxml import etree

url = "https://www.biquge5200.cc/xuanhuanxiaoshuo/"


response = requests.get(url).text
# print(response)

mytree = lxml.etree.HTML(response)

level2List = mytree.xpath("//div[@class='r']//li")

for i in level2List:
    level2 = i.xpath("./span/a/text()")[0]
    level2Url = i.xpath("./span/a/@href")[0]
    author = i.xpath("./span[2]/text()")[0]
    print(level2,level2Url, author)