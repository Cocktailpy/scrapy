# -*- coding: utf-8 -*-
import scrapy
import requests
import lxml
from lxml import etree

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

# from scrapy import log # 日志,已经被弃用

from dongguan import items

import logging  # 日志模块


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 设置输出格式
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"  # 设置时间格式
logging.basicConfig(filename='dgggg.log', filemode='a+', format=LOG_FORMAT, datefmt=DATE_FORMAT)


class DgSpider(CrawlSpider):
    name = 'dg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=30']

    rules = [Rule(LinkExtractor(allow=("page=(\d+)")), follow=True, callback="get_parse")]

    # log.msg("我是日志")



    def get_parse(self, response):
        logging.info("开始爬取")
        qList = response.xpath("//table[@bgcolor=\"#FBFEFF\"]//tr")
        for q in qList:
            item = items.DongguanItem()

            qnum = q.xpath("./td[1]/text()")[0].extract()  # 编号
            qtype = q.xpath("./td[2]/a[1]/text()")[0].extract()[1:-1]  # 类型
            qtitle = q.xpath("./td[2]/a[2]/text()")[0].extract()  # 标题
            qurl = q.xpath("./td[2]/a[2]/@href")[0].extract()
            qcontent = self.get_content(qurl)  # 问题描述
            qstatus = q.xpath("./td[3]/span/text()")[0].extract()  # 状态
            ifriend = q.xpath("./td[4]/text()")[0].extract()  # 网友
            qtime = q.xpath("./td[5]/text()")[0].extract()  # 时间

            # print(qnum, qtype, qcontent, qtime, "===============")

            item["qnum"] = qnum  # 编号
            item["qtype"] = qtype
            item["qtitle"] = qtitle
            item["qcontent"] = qcontent
            item["qstatus"] = qstatus
            item["ifriend"] = ifriend
            item["qtime"] = qtime

            logging.error("错了")
            yield item

    logging.info("爬虫结束")

    def get_content(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

        response = requests.get(url, headers=headers).content.decode('gbk')

        # print(response)
        mytree = lxml.etree.HTML(response)

        content = mytree.xpath("//div[@class='c1 text14_2']//text()")[0].replace("\xa0", '').strip()
        return content
