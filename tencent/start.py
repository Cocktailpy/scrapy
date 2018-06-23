#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/6/5 10:33
@Author  : Fate
@File    : start.py
'''


import scrapy.cmdline

def main():
    scrapy.cmdline.execute(["scrapy", "crawl", "mytencent"])

if __name__ == '__main__':
    main()