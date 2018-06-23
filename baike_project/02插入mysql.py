#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/6/7 15:22
@Author  : Fate
@File    : 02插入mysql.py
'''

import pymysql
import redis

import json

# 连接mysql
mysqlcli = pymysql.connect(host='127.0.0.1', user='root', password="123456",
                           database='fate', port=3306,
                           charset='utf8')

# 游标
cur = mysqlcli.cursor()
# 连接redis
myrediscli = redis.Redis(host='10.3.132.16', port=6379,
                         db=0, password='123456')

while True:
    # blpop() 队列模式
    # brpop() 栈模式
    source, data = myrediscli.blpop(["mybaike_redis:items"])

    item = json.loads(data)
    cols, values = zip(*item.items())

    sql = "insert into `%s`(%s) values (%s)" % ('baike', ','.join(cols), ','.join(['%s'] * len(values)))

    print(sql)
    cur.execute(sql, values)  # 执行
    mysqlcli.commit()  # 提交
    print(cur._last_executed)  # 上一条执行语句
