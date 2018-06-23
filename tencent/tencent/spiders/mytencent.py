# -*- coding: utf-8 -*-
import scrapy
from tencent import items

from scrapy.spiders import Rule, CrawlSpider  # 提取规则
from scrapy.linkextractors import LinkExtractor  # 提取连接


# 继承CrawlSpider
class MytencentSpider(CrawlSpider):
    name = 'mytencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    # 爬取规则
    # LinkExtractor() 提取规则 allow 允许的连接使用正则匹配
    # follow 跟踪 True则跟踪，False则不跟踪
    # callback 调用
    rules = [Rule(LinkExtractor(allow=("start=(\d+)")), follow=True, callback="get_parse")]

    # 一定不能用parse()
    def get_parse(self, response):
        jobList = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for job in jobList:
            item = items.TencentItem()

            jobName = job.xpath("./td[1]/a/text()")[0].extract()  # 提取实际内容
            print(jobName, "========================")
            jobType = job.xpath("./td[2]/text()")[0].extract()
            jobNum = job.xpath("./td[3]/text()")[0].extract()
            jobAddr = job.xpath("./td[4]/text()")[0].extract()
            ptime = job.xpath("./td[5]/text()")[0].extract()

            item["jobName"] = jobName
            item["jobType"] = jobType
            item["jobNum"] = jobNum
            item["jobAddr"] = jobAddr
            item["ptime"] = ptime

            yield item
