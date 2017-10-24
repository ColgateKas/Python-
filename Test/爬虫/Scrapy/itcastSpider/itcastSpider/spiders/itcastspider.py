# -*- coding: utf-8 -*-
import scrapy
from itcastSpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        #with open('teacher.html','wb') as f:
        #    f.write(response.body)
        #通过xpath获取所有老师的列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []
        for each in teacher_list:
            item = ItcastItem()
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            teacherItem.append(item)
        return teacherItem