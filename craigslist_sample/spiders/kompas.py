from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from craigslist_sample.items import KompasBolaItem, KompasNasionalItem


class KompasNasionalSpider(BaseSpider):
   name = "kompasnasional"
   allowed_domains = ["http://nasional.kompas.com/"]
   start_urls = [
       "http://nasional.kompas.com/indeks/1",
       "http://nasional.kompas.com/indeks/2",
       "http://nasional.kompas.com/indeks/3",
       "http://nasional.kompas.com/indeks/4",
       "http://nasional.kompas.com/indeks/5",
       "http://nasional.kompas.com/indeks/6",
       "http://nasional.kompas.com/indeks/7",
       "http://nasional.kompas.com/indeks/8",
       "http://nasional.kompas.com/indeks/9",
       "http://nasional.kompas.com/indeks/10",     
   ]
   def parse(self, response): 
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//*[@id="leftside"]/div[2]/ul/li')
       items = []
       for site in sites:
           item = KompasNasionalItem()              
           title = site.select('div[3]/a/text()').extract_first()
           link = site.select('div[3]/a/@href').extract_first()
           img = site.select('div[1]/img/@src').extract_first()
           desc = site.select('div[4]/text()').extract_first()           
           item['title'] = title
           item['category'] = 'nasional'
           item['link'] = link
           item['img'] = img
           item['desc'] = desc
           items.append(item)
       return items

class KompasBolaSpider(BaseSpider):
   name = "kompasbola"
   allowed_domains = ["http://bola.kompas.com/ligaindonesia/"]
   start_urls = [
       "http://bola.kompas.com/ligaindonesia/1",
       "http://bola.kompas.com/ligaindonesia/2",
       "http://bola.kompas.com/ligaindonesia/3",
       "http://bola.kompas.com/ligaindonesia/4",
       "http://bola.kompas.com/ligaindonesia/5",
       "http://bola.kompas.com/ligaindonesia/6",
       "http://bola.kompas.com/ligaindonesia/7",
       "http://bola.kompas.com/ligaindonesia/8",
       "http://bola.kompas.com/ligaindonesia/9",
       "http://bola.kompas.com/ligaindonesia/10",
   ]

   def parse(self, response): 
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/ul/li')
       items = []

       for site in sites:
           item = KompasBolaItem()

           item ['title'] = site.select('div/h3/a/text()').extract_first()
           item ['category'] = 'bola'
           item ['link'] = site.select('div/h3/a/@href').extract_first()
           item ['img'] = site.select('div/img/@src').extract_first()
           item ['desc'] = site.select('div/p/text()').extract_first()
           items.append(item)
       return items
