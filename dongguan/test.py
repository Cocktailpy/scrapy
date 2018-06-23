#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/6/5 14:25
@Author  : Fate
@File    : test.py
'''


import requests
import lxml
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

response = requests.get(url="http://wz.sun0769.com/html/question/201806/373491.shtml",headers=headers).content.decode('gbk')

# print(response)
mytree = lxml.etree.HTML(response)

content = mytree.xpath("//div[@class='c1 text14_2']//text()")[0].replace("\xa0",'').strip()
print(content)