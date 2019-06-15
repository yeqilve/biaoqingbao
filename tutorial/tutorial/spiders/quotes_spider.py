import scrapy

class quotes_spider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'https://www.baidu.com'
    ]

    def parse(self, response):
        filename = 'quotes.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)