# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CraigslistSampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ContohItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class KompasNasionalItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    desc = Field()

class KompasBolaItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    desc = Field()

class BhinekaHandphoneItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    price = Field()
    web = Field()

class BukalapakHandphoneItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    price = Field()
    web = Field()

class MatahariHandphoneItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    price = Field()
    web = Field()

class TokopediaHandphoneItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    price = Field()
    web = Field()

class MangakuOnePieceItem(Item):
    title = Field()
    category = Field()
    link = Field()
    img = Field()
    price = Field()
    web = Field()