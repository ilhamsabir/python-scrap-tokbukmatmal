# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class CraigslistSamplePipeline(object):
#     def process_item(self, item, spider):
#         return item


# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy import log



# class MongoDBPipeline(object):
class CraigslistSamplePipeline(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item

# class Bhineka(object):
class BhinekaPipe(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_PRODUCT_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_PRODUCT_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item

# class bukalapak(object):
class BukalapakPipe(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_PRODUCT_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_PRODUCT_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item

# class Matahari(object):
class MatahariPipe(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_PRODUCT_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_PRODUCT_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item

# class Matahari(object):
class TokopediaPipe(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_PRODUCT_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_PRODUCT_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item

# class Matahari(object):
class MangakuOnepiecePipe(object):  
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_MANGA_COLLECTION']]    
        # self.collection.get(type(item)).insert(item, continue_on_error=True)

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['MONGODB_DATABASE'],
            settings['MONGODB_PRODUCT_COLLECTION'],
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']))
        return item