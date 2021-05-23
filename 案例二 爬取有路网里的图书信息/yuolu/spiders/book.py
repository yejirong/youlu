# -*- coding: utf-8 -*-
'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import scrapy
from yuolu.items import YuoluItem
from scrapy.selector import Selector
from scrapy.http import Request
from fake_useragent import UserAgent


class BookSpider(scrapy.Spider):
    name = 'book'  # 项目名字，唯一(必要)
    # allowed_domains = ['youlu.net']
    # 爬取的主页
    start_urls = ['https://www.youlu.net/classify/2-0101-4138-1.html']  # 语言与编程
    # start_urls = ['https://www.youlu.net/classify/2-0115-1827-1.html']  # 计算机理论基础
    # start_urls = ['https://www.youlu.net/classify/2-0106-1802-1.html']  # 数据库
    # start_urls = ['https://www.youlu.net/classify/2-0105-1558-1.html']  # 网页制作
    # start_urls = ['https://www.youlu.net/classify/2-0103-1481-1.html']  # 图形图像
    # start_urls = ['https://www.youlu.net/classify/2-0102-1285-1.html']  # 软件工程
    # start_urls = ['https://www.youlu.net/classify/2-0117-1119-1.html']  # 网络与通信
    # start_urls = ['https://www.youlu.net/classify/2-0114-1062-1.html']  # 单片机与嵌入式
    # start_urls = ['https://www.youlu.net/classify/2-0107-1012-1.html']  # 操作系统
    # start_urls = ['https://www.youlu.net/classify/2-0114-1062-1.html']  # 会计审计统计
    # start_urls = ['https://www.youlu.net/classify/2-0304-2644-1.html']  # 经济学理论
    # start_urls = ['https://www.youlu.net/classify/2-0411-4241-1.html']  # 机械仪表工程
    # start_urls = ['https://www.youlu.net/classify/2-0401-3423-1.html']  # 电子通信
    # start_urls = ['https://www.youlu.net/classify/2-0409-2287-1.html']  # 电工电子
    # start_urls = ['https://www.youlu.net/classify/2-0703-4375-1.html']  # 设计
    # start_urls = ['https://www.youlu.net/classify/2-2201-3828-1.html']  # 数学
    # start_urls = ['https://www.youlu.net/classify/2-2203-2025-1.html']  # 化学
    # start_urls = ['https://www.youlu.net/classify/2-0315-1810-4.html']  # 国际贸易

    ua = UserAgent()  # 随机userUserAgent
    print(ua)

    def parse(self, response):
        item = YuoluItem()  # 生成一个item对象
        selector = Selector(response)  # 定义选择器
        infos = selector.xpath('.//div[@class="newBookList"]/ul/li')  # 用xpath定位到ul标签下所有li标签
        for info in infos:
            name = info.xpath('div[2]/div[1]/a/text()').extract()[0]  # 书籍名字
            link = info.xpath('div[1]/a/@href').extract()[0]  # 爬取a标签里的href用于拼接
            book_link = str('https://www.youlu.net' + link)  # 书籍链接
            author = info.xpath('div[2]/div[2]/text()').extract()[0]   # 作者
            press = info.xpath('div[2]/div[2]/text()').extract()[0]  # 出版社
            press_data = info.xpath('div[2]/div[2]/text()').extract()[0]  # 出版时间
            number = info.xpath('div[2]/div[2]/text()').extract()[0]  # 书籍页数
            weight = info.xpath('div[2]/div[2]/text()').extract()[0]  # 书籍重量
            new_price = info.xpath('div[2]/div[4]/span[1]/text()').extract()[0]  # 新书价格
            price = info.xpath('div[2]/div[4]/span[2]/text()').extract()[0]  # 旧书价格
            save = info.xpath('div[2]/div[4]/span[3]/text()').extract()[0]  # 节约
            resume = info.xpath('div[2]/div[3]/text()').extract()[0]  # 简述
            # 赋值对象成员变量
            item['name'] = name
            item['book_link'] = book_link
            item['author'] = author.split('/')[0]
            item['press'] = press.split('/')[1]
            item['press_data'] = press_data.split('/')[2]
            item['number'] = number.split('/')[3]
            item['weight'] = weight.split('/')[4]
            item['new_price'] = new_price
            item['price'] = price
            item['save'] = save
            item['resume'] = resume.split('\n')[1]

            yield item
        # 爬取所有页数
        urls = ['https://www.youlu.net/classify/2-0101-4138-{}.html'.format(str(i)) for i in range(2, 207)]  # 语言与编程
        # urls = ['https://www.youlu.net/classify/2-0115-1827-{}.html'.format(str(i)) for i in range(2, 92)]  # 计算机理论基础
        # urls = ['https://www.youlu.net/classify/2-0106-1802-{}.html'.format(str(i)) for i in range(4, 90)]  # 数据库
        # urls = ['https://www.youlu.net/classify/2-0105-1558-{}.html'.format(str(i)) for i in range(5, 78)]  # 网页制作
        # urls = ['https://www.youlu.net/classify/2-0103-1481-{}.html'.format(str(i)) for i in range(2, 75)]  # 图形图像
        # urls = ['https://www.youlu.net/classify/2-0102-1285-{}.html'.format(str(i)) for i in range(2, 65)]  # 软件工程
        # urls = ['https://www.youlu.net/classify/2-0117-1119-{}.html'.format(str(i)) for i in range(2, 56)]  # 网络与通信
        # urls = ['https://www.youlu.net/classify/2-0114-1062-{}.html'.format(str(i)) for i in range(2, 54)]  # 单片机与嵌入式
        # urls = ['https://www.youlu.net/classify/2-0107-1012-{}.html'.format(str(i)) for i in range(2, 51)]  # 操作系统
        # urls = ['https://www.youlu.net/classify/2-0308-4859-{}.html'.format(str(i)) for i in range(2, 243)]  # 会计审计统计
        # urls = ['https://www.youlu.net/classify/2-0304-2644-{}.html'.format(str(i)) for i in range(2, 133)]  # 经济学理论
        # urls = ['https://www.youlu.net/classify/2-0411-4241-{}.html'.format(str(i)) for i in range(2, 213)]  # 机械仪表工程
        # urls = ['https://www.youlu.net/classify/2-0401-3423-{}.html'.format(str(i)) for i in range(2, 172)]  # 电子通信
        # urls = ['https://www.youlu.net/classify/2-0409-2287-{}.html'.format(str(i)) for i in range(2, 172)]  # 电工电子
        # urls = ['https://www.youlu.net/classify/2-0703-4375-{}.html'.format(str(i)) for i in range(2, 219)]  # 设计
        # urls = ['https://www.youlu.net/classify/2-2201-3828-{}.html'.format(str(i)) for i in range(2, 192)]  # 数学
        # urls = ['https://www.youlu.net/classify/2-2203-2025-{}.html'.format(str(i)) for i in range(2, 192)]  # 化学
        # urls = ['https://www.youlu.net/classify/2-0315-1810-{}.html'.format(str(i)) for i in range(5, 91)]  # 国际贸易
        for url in urls:
            yield Request(url, callback=self.parse, headers={'User-Agent': self.ua.random})

