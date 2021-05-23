# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YuoluItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 书籍名字
    book_link = scrapy.Field()  # 书籍链接
    author = scrapy.Field()  # 作者
    press = scrapy.Field()  # 出版社
    press_data = scrapy.Field()  # 出版时间
    number = scrapy.Field()  # 书籍页数
    weight = scrapy.Field()  # 书籍重量
    new_price = scrapy.Field()  # 新书价格
    price = scrapy.Field()  # 旧书价格
    save = scrapy.Field()  # 节约
    resume = scrapy.Field()  # 简述
