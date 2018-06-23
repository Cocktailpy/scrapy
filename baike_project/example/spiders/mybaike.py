# -*- coding: utf-8 -*-
import scrapy

from example import items

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class MybaikeSpider(CrawlSpider):
    name = 'mybaike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['http://baike.baidu.com/item/Java/85979']

    rules = [Rule(LinkExtractor(allow=("item/(.*)")), follow=True, callback="get_parse")]

    def get_parse(self, response):
        item = items.BaikeItem()
        kw = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0].extract()  # 关键字

        ktype = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h2/text()")# 类型
        if len(ktype) == 0:
            ktype = "待编辑"
        else:
            ktype = ktype[0].extract()
        contentList = response.xpath("//div[@class=\"lemma-summary\"]//text()")
        content = ""

        for c in contentList:
            content += c.extract().strip()

        item["kw"] = kw
        item["ktype"] = ktype
        item["content"] = content

        yield item
