# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        each_line = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        item = TencentItem()
        for each in each_line:
            #职位名称
            item['positionName'] = each.xpath("./td[1]/a/text()").extract_first()
            #职位链接
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract_first()
            #职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract_first()
            #招聘人数
            item['positionPeple'] = each.xpath("./td[3]/text()").extract_first()
            #工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract_first()
            #发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract_first()

            yield item
        if self.offset < 2370:
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
