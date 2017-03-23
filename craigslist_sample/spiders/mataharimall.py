from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from craigslist_sample.items import MatahariHandphoneItem


class MatahariHandphoneSpider(BaseSpider):
   name = "mataharihandphone"
   allowed_domains = ["https://www.mataharimall.com/p-1/handphone-tablet"]
   start_urls = [
       "https://www.mataharimall.com/p-1/handphone-tablet?page=2",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=3",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=4",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=5",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=6",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=7",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=8",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=9",
       "https://www.mataharimall.com/p-1/handphone-tablet?page=10"
   ]
   
   def parse(self, response): 
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//*[@id="block-system-main"]/div/div[1]/div/div[2]/div[1]/div/div')
       items = []
       for site in sites:
           item = MatahariHandphoneItem()  
                       
           title = site.select('div/a/div/div[3]/div[1]/text()').extract_first()
           link = site.select('div/a/@href').extract_first()
           img = site.select('div/a/div/div[2]/span/img/@data-src').extract_first()         
           price = site.select('div/a/div/div[3]/div[2]/div[2]/text()').extract_first()
   
           item['title'] = title
           item['category'] = 'handpone'
           item['link'] = link
           item['img'] = img
           item['price'] = price
           item['web'] = 'www.mataharimall.com'
           items.append(item)
       return items
