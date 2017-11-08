# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencentCrawl'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        each_line = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for each in each_line:
            item = TencentItem()
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
