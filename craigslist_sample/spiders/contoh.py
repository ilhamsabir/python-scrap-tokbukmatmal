# # -*- coding: utf-8 -*-
# import scrapy


# class ContohSpider(scrapy.Spider):
#     name = "contoh"
#     allowed_domains = ["http://sfbay.craigslist.org/search/npo"]
#     start_urls = ['http://http://sfbay.craigslist.org/search/npo/']

#     def parse(self, response):
#         pass

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from craigslist_sample.items import ContohItem

class ContohSpider(BaseSpider):
   name = "contoh"
   allowed_domains = ["dmoz.org"]
   start_urls = [
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//ul/li')
       items = []
       for site in sites:
           item = ContohItem()
           item['title'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select('text()').extract()
           items.append(item)
       return items