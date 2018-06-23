# -*- coding: utf-8 -*-
import scrapy


class MyzhihuSpider(scrapy.Spider):
    name = 'myzhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/signup?next=%2F',
                  "https://www.zhihu.com/people/zuo-zai-fen-tou-diao-xi-gui-82/activities"]

    def __init__(self):
        self.browser = None  # selenium
        self.cookies = None  # 存储cookies
        super(MyzhihuSpider, self).__init__()

    def parse(self, response):
        print("**" * 30, response.url)
        print(response.body.decode('utf-8', 'ignore'))


        pass
