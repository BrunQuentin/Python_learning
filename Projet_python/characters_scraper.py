import scrapy
from scrapy.selector import Selector


class BlogSpider(scrapy.Spider)
    name= 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d\'animation']

    def parse(self, response)
        for link in reponse.css('div#mw-pages div.mw-content-ltr li'):
            yield {'': link.css('a ::text').extract_first()}
