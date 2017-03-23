from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from craigslist_sample.items import MangakuOnePieceItem


class MatahariHandphoneSpider(BaseSpider):
   name = "mangaone"
   start_urls = [
        'http://mangaku.web.id/one-piece-chapter-852-kegagagalan-germa/'
    ]

    def parse(self, response):
        for mangaop in response.css('div.separator'):
            yield {
                'imgsrc': mangaop.css('a.img::src').extract_first(),                
            }

        next_page = response.css('a.img::attr("src")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
