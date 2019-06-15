import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    start_urls = ["https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B1%ED%C7%E9%B0%FC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"]

    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'w').write(response.body)