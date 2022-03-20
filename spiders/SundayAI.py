import scrapy
from bs4 import BeautifulSoup

class SundayaiSpider(scrapy.Spider):
    name = 'SundayAI'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']

    def parse(self, response):
        pass
