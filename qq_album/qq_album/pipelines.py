# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

myclient = pymongo.MongoClient('mongodb://zh017/qq_music')
mydb = myclient['qq_music']

# 专辑表
mycol = mydb['album_detail']

# mycol = pymongo.MongoClient('127.0.0.1')['ssss']['aaaaaaa']

class QqAlbumPipeline(object):
    def process_item(self, item, spider):
        mycol.insert(dict(item))
        return item
