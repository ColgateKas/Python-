# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem


class Dongguanspdier2Spider(scrapy.Spider):
    name = 'dongguanSpider2'
    #allowed_domains = ['wz.sun0769.com']
    url = 'http://d.wz.sun0769.com/index.php/department?departmentid=63&status=&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        #每页所有帖子的链接集合
        links = response.xpath(
            '//div[@class="pagecenter"]/table//td/a[@class="news14"]/@href'
        ).extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        if self.offset <= 10980:
            self.offset += 18
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)




    def parse_item(self, response):
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