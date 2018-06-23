# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class BaikeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # table_name = scrapy.Field()
    kw = Field()  # 关键字
    ktype = Field()  # 类型
    content = Field()  # 描述
    # crawled = Field()  # 爬取时间
    # spider = Field()  # 爬虫名


class ExampleItem(Item):
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()


class ExampleLoader(ItemLoader):
    default_item_class = ExampleItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
