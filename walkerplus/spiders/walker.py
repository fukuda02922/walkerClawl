# -*- coding: utf-8 -*-
import scrapy


class WalkerSpider(scrapy.Spider):
    name = 'walker'
    allowed_domains = ['www.walkerplus.com']
    start_urls = [
        top_url + 'spot_list/'
    ]
    top_url = 'http://www.walkerplus.com/'

    def parse(self, response):

        pass
