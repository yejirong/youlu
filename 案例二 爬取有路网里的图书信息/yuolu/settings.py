# -*- coding: utf-8 -*-

# Scrapy settings for yuolu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yuolu'

SPIDER_MODULES = ['yuolu.spiders']
NEWSPIDER_MODULE = 'yuolu.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
#
# USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3' \
#              ' (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 5
DOWNLOADER_MIDDLEWARES = {
   # 'yuolu.middlewares.YuoluDownloaderMiddleware': 543,
    'yuolu.middlewares.MyproxiesSipderMIddleware':125
}
ITEM_PIPELINES = {
   'yuolu.pipelines.YuoluPipeline': 300,
}

IPOOL = [

    {"ipaddr": "36.249.118.9:9999"},
    {"ipaddr": "116.196.85.150:3128"},
    {"ipaddr": "61.135.217.7:80"},
    {"ipaddr": "112.253.11.113:8000"},
    {"ipaddr": "116.196.85.150:3128"},
    {"ipaddr": "39.137.69.9:80"},
    {"ipaddr": "124.200.36.118:40188"},
    {"ipaddr": "59.36.10.79:3128"},
    {"ipaddr": "121.8.146.99:8060"},
    {"ipaddr": "121.17.210.114:8060"},
    {"ipaddr": "124.90.49.146:8888"},
    {"ipaddr": "221.2.175.238:8060"},
    {"ipaddr": "113.161.116.90:8080"},
    {"ipaddr": "114.104.143.48:9999"},
    {"ipaddr": "110.243.20.23:9999"},
    {"ipaddr": "115.221.244.42:9999"},
    {"ipaddr": "123.56.118.36:8080"},
    {"ipaddr": "115.29.199.16:8118"}
]
# FEED_URL = 'file:d:/yjr'
# FEED_FORMAT = 'csv'
# FEED_EXPORT_FIELDS = ['书籍名字', '书籍链接', '作者', '出版社', '书籍链接', '书籍页数',
#                       '书籍重量', '新书价格', '旧书价格', '节约', '简述']

# Crawl responsibly by identifying yourself (and your website) on the user-agent


# Obey robots.txt rules


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yuolu.middlewares.YuoluSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
