# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# fifo 队列模式，先进先出
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈模式，先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# DOWNLOAD_DELAY = 1
# REDIS_HOST = '10.3.132.12'
# REDIS_PORT = 6379

REDIS_URL = "redis://:123456@10.3.132.16:6379"

#DOWNLOADER_MIDDLEWARES = {
#    'baike.middlewares.MyCustomDownloaderMiddleware': 543,
#}