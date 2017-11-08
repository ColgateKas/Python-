# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json


class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuSpider'
    allowed_domains = ['capi.douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        each_line = json.loads(response.text)["data"]
        for each in each_line:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['imgLink'] = each['vertical_src']
            yield item
        if self.offset < 200:
            self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
