# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        each_line = response.xpath('//div[@class="info"]')
        for line in each_line:
            item = DoubanItem()
            item['title'] = line.xpath(
                './/span[@class="title"][1]/text()').extract()[0]
            item['bd'] = line.xpath('.//div[@class="bd"]/p/text()').extract()[
                0]
            item['start'] = line.xpath(
                './/span[@class="rating_num"]/text()').extract_first()
            item['quote'] = line.xpath(
                './/p[@class="quote"]/span/text()').extract_first()

            yield item
        if (self.offset < 225):
            self.offset += 25
            yield scrapy.Request(
                self.url + str(self.offset), callback=self.parse)
