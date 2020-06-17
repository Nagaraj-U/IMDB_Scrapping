# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo
import sqlite3
class MongodbPipeline(object):
    collection_name="best_movies"
    # @classmethod
    # def from_crawler(cls,crawler):
    #     logging.warning(crawler.settings.get("mongo_uri"))

    def open_spider(self,spider):
        self.client=pymongo.MongoClient("mongodb+srv://nagaraj:123@cluster0-qu8sr.mongodb.net/IMDB?retryWrites=true&w=majority")
        self.db=self.client["IMDB"]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db["collection_name"].insert(item)
        return item


# class SQLlitePipeline(object):

#     def open_spider(self,spider):
#         self.connection=sqlite3.connect("imdb.db")
#         self.c=self.connection.cursor()
#         try:
#             self.c.execute('''
#                 CREATE TABLE best_movies(
#                     title TEXT,
#                     year TEXT,
#                     duration TEXT,
#                     genre TEXT,
#                     rating TEXT
#                 )
#                 ''')
#             self.connection.commit()
#         except sqlite3.OperationalError:
#             pass

#     def close_spider(self,spider):
#         self.connection.close()

#     def process_item(self, item, spider):
#         self.c.execute('''
#         INSERT INTO best_movies(title,year,duration,genre,rating) VALUES(?,?,?,?,?)
#         ''',(
#             item.get('Title'),
#             item.get('Year'),
#             item.get('Duration'),
#             item.get('Genre'),
#             item.get('Rating'),
#         ))
#         self.connection.commit()
#         return item
