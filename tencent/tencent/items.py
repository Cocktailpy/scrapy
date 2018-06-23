# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()  # 职位名称
    jobType = scrapy.Field()  # 职位类型
    jobNum = scrapy.Field()  # 职位数量
    jobAddr = scrapy.Field()  # 工作地点
    ptime = scrapy.Field()  # 发布时间
    pass
