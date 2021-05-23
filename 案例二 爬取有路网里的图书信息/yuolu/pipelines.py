# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#
# class YuoluPipeline:
#
#     def process_item(self, item, spider):
#         return item
'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import pandas as pd


class YuoluPipeline(object):

    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item), index=[0])  # item数据转换为字典格式
        # 将数据保存到本地csv文件中
        data.to_csv("./语言与编程.csv", mode='a+', index=None, header=None)  # 语言与编程
        # data.to_csv("./计算机理论基础.csv", mode='a+', index=None, header=None)  # 计算机理论基础
        # data.to_csv("./数据库.csv", mode='a+', index=None, header=None)  # 数据库
        # data.to_csv("./网页制作.csv", mode='a+', index=None, header=None)  # 网页制作
        # data.to_csv("./图形图像.csv", mode='a+', index=None, header=None)  # 图形图像
        # data.to_csv("./软件工程.csv", mode='a+', index=None, header=None)  # 软件工程
        # data.to_csv("./网络与通信.csv", mode='a+', index=None, header=None)  # 网络与通信
        # data.to_csv("./单片机与嵌入式.csv", mode='a+', index=None, header=None)  # 单片机与嵌入式
        # data.to_csv("./操作系统.csv", mode='a+', index=None, header=None)  # 操作系统
        # data.to_csv("./会计审计统计.csv", mode='a+', index=None, header=None)  # 会计审计统计
        # data.to_csv("./经济学理论.csv", mode='a+', index=None, header=None)  # 经济学理论
        # data.to_csv("./机械仪表工程.csv", mode='a+', index=None, header=None)  # 机械仪表工程
        # data.to_csv("./电子通信.csv", mode='a+', index=None, header=None)  # 电子通信
        # data.to_csv("./电工电子.csv", mode='a+', index=None, header=None)  # 电工电子
        # data.to_csv("./设计.csv", mode='a+', index=None, header=None)  # 设计
        # data.to_csv("./数学.csv", mode='a+', index=None, header=None)  # 数学
        # data.to_csv("./化学.csv", mode='a+', index=None, header=None)  # 化学
        # data.to_csv("./国际贸易.csv", mode='a+', index=None, header=None)  # 国际贸易
        return item

# from openpyxl import Workbook
#
#
# class YuoluPipeline(object):
#     wb = Workbook()
#     ws = wb.active
#     # 设置表头
#     ws.append(['书籍名字', '书籍链接', '作者', '出版社', '书籍链接', '书籍页数',
#                '书籍重量', '新书价格', '旧书价格', '节约', '简述'])
#
#     def process_item(self, item, spider):
#         # 添加数据
#         line = [item['name'], item['book_link'], item['author'], item['press'], item['press_data'], item['number'],
#                 item['weight'], item['new_price'], item['price '], item['save'], item['resume']]
#         self.ws.append(line)  # 按行添加
#         self.wb.save('book.xlsx')
#         return item


