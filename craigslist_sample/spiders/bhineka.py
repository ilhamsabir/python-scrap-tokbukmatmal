from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from craigslist_sample.items import BhinekaHandphoneItem


class BhinekaHandphoneSpider(BaseSpider):
   name = "bhinekahandphone"
   allowed_domains = ["http://www.bhinneka.com/category/smart_phone.aspx"]
   start_urls = [
       "http://www.bhinneka.com/category/smart_phone.aspx?page=1",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=2",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=3",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=4",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=5",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=6",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=7",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=8",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=9",
       "http://www.bhinneka.com/category/smart_phone.aspx?page=10"   
   ]
   
   def parse(self, response): 
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//*[@id="products"]/ul/li')
       items = []
       for site in sites:
           item = BhinekaHandphoneItem()  
                       
           title = site.select('a/span/span[1]/text()').extract_first() 
           link = site.select('a/@href').extract_first()
           img = site.select('a/img/@src').extract_first()
           price = site.select('div[1]/span/span[2]/text()').extract_first()
          
           item['title'] = title
           item['category'] = 'handpone'
           item['link'] = link
           item['img'] = img
           item['price'] = price
           item['web'] = 'www.bhineka.com'
           items.append(item)
       return items
