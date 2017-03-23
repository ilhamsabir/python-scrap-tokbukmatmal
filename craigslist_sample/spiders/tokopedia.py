import scrapy


class TokopediaSpider(scrapy.Spider):
    name = "tokopediahandphone"
    start_urls = [
        'https://www.tokopedia.com/p/handphone-tablet/handphone',
    ]

    def parse(self, response):
        for site in response.css('div.product'):
            yield {               
                'title': site.css('div.meta-product.div.name.b.text::text').extract_first(),
                'category': 'handphone',
                'link': site.css('a.href::text').extract_first(),
                'img':site.css('div.product-hover.div.product-image.img.src::text').extract_first(),
                'price': site.css('div.meta-product.div.row-fluid.div.span8.span.text::text').extract_first(),
                'web': 'www.tokopedia.com'         
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)