# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class DongguanPipeline(object):

    def open_spider(self, spider):
        # 连接数据库
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password="123456",
                                    database='fate',
                                    port=3306,
                                    charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO dg(qnum,qtype,qtitle,qcontent,qstatus,ifriend,qtime) VALUES (%s,%r,%r,%r,%r,%r,%r)" % (
            item["qnum"], item["qtype"], item["qtitle"], item["qcontent"], item["qstatus"], item["ifriend"],
            item["qtime"])

        print(sql, "********************")
        self.cursor.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
