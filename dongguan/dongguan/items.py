# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qnum = scrapy.Field()  # 编号
    qtype = scrapy.Field()  # 类型
    qtitle = scrapy.Field()  # 标题
    qcontent = scrapy.Field()  # 问题描述
    qstatus = scrapy.Field()  # 状态
    ifriend = scrapy.Field()  # 网友
    qtime = scrapy.Field()  # 时间

    pass
