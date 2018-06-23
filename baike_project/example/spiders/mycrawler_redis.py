from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from example import items

class MyBaikeCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mybaike_redis'
    redis_key = 'mybaike:start_urls'

    rules = [Rule(LinkExtractor(allow=("item/(.*)")), follow=True, callback="get_parse")]


    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('baike.baidu.com', 'baidu.com')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyBaikeCrawler, self).__init__(*args, **kwargs)

    def get_parse(self, response):
        item = items.BaikeItem()
        kw = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0].extract()  # 关键字

        ktype = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h2/text()")  # 类型
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

