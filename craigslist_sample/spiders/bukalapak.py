from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from craigslist_sample.items import BukalapakHandphoneItem


class BukalapakHandphoneSpider(BaseSpider):
   name = "bukalapakhandphone"
   allowed_domains = ["https://www.bukalapak.com/c/handphone/hp-smartphone"]
   start_urls = [
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=2",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=3",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=4",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=5",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=6",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=7",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=8",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=9",
       "https://www.bukalapak.com/c/handphone/hp-smartphone?page=10"
   ]
   
   def parse(self, response): 
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//*[@id="display_product_search"]/div[2]/ul/li')
       items = []
       for site in sites:
           item = BukalapakHandphoneItem()  
                       
           title = site.select('div/article/div[3]/h3/a/text()').extract_first()        
           link = site.select('div/article/div[3]/h3/a/@href').extract_first()       
           img = site.select('div/article/div[1]/a/img/@src').extract_first()
           price = site.select('div/article/div[3]/div[2]/span[1]/span[2]/text()').extract_first()
          
           item['title'] = title
           item['category'] = 'handpone'
           item['link'] = link
           item['img'] = img
           item['price'] = price
           item['web'] = 'www.bukalapak.com'
           items.append(item)
       return items
