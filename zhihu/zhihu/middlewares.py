# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver

import time
import requests

from scrapy.http import HtmlResponse  # 响应


class LoginMiddleware(object):
    def process_request(self, request, spider):
        '''
        请求前
        :param request: 请求
        :param spider: 爬虫名
        :return:
        '''
        # 判读是哪个爬虫
        if spider.name == "myzhihu":
            # 判读是否是登陆
            if request.url.find("signup") != -1:
                # 创建Chrome对象
                spider.browser = webdriver.Chrome()
                # 打开请求url
                spider.browser.get(request.url)
                spider.browser.find_element_by_xpath("//div[@class=\"SignContainer-switch\"]/span").click()

                # 用户名
                username = spider.browser.find_element_by_name("username")
                username.send_keys("18588403840")
                # 密码
                password = spider.browser.find_element_by_name("password")
                password.send_keys("Changeme_123")

                time.sleep(6)

                # 登陆
                spider.browser.find_element_by_xpath(
                    "//button[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()
                time.sleep(2) # 防止打印登录前的密码
                print("==" * 30, spider.browser.current_url)

                # 获取cookie
                spider.cookies = spider.browser.get_cookies()

                return HtmlResponse(url=spider.browser.current_url,  # 当前url
                                    body=spider.browser.page_source,  # html源码
                                    encoding='utf-8')


            else:
                # 用selenium，速度慢
                # 使用requests
                # 存储cookie
                session = requests.session()

                for cookie in spider.cookies:
                    session.cookies.set(cookie['name'], cookie['value'])

                session.headers.clear() # 清空头

                newpage = session.get(request.url, verify=False).text

                return HtmlResponse(url=request.url,
                                    body=newpage,
                                    encoding='utf-8')



class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
