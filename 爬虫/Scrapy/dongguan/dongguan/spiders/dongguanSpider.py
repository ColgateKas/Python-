# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class DongguanspiderSpider(CrawlSpider):
    name = 'dongguanSpider'
    #allowed_domains = ['wz.sun0769.com']
    start_urls = [
        'http://d.wz.sun0769.com/index.php/department?departmentid=63&status=&page=0'
    ]

    #没有callback，follow默认会为True 意味着继续跟进
    rules = (Rule(LinkExtractor(allow=r'status=&page=\d+')), Rule(
        LinkExtractor(allow=r'/question/\d+/\d+.shtml'),
        callback='parse_item',
        follow=False), Rule(
            LinkExtractor(allow=r'show\?id=\d+'),
            callback='parse_item',
            follow=False), )

    def parse_item(self, response):
        print(response.url)
        content = ''.join(
            response.xpath('//div[@class="contentext"]/text()')
            .extract()).replace(u'\xa0', '').strip()
        if len(content) == 0:
            content = ''.join(
                response.xpath('//div[@class="c1 text14_2"]/text()')
                .extract()).replace(u'\xa0', '').strip()
        item = DongguanItem()
        item['title'] = response.xpath(
            '//div[@class="pagecenter p3"]//strong/text()').extract_first(
            ).replace(u'\xa0', ' ').strip()
        item['num'] = item['title'].split(':')[-1].strip()
        item['content'] = content
        item['url'] = response.url
        yield item
