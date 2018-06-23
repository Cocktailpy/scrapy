# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):

    def open_spider(self, spider):
        self.f = open("tencent.txt", 'w', encoding='utf-8', errors='ignore')
    def process_item(self, item, spider):

        self.f.write(str((item['jobName'], item["jobType"], item["jobNum"], item["jobAddr"], item["ptime"])) + '\n')
        self.f.flush()

        return item
    def close_spider(self, spider):
        self.f.close()
