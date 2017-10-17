import scrapy
from scrapyDemo.items import ScrapydemoItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/'
        ]

    def parse(self, response):
        sites = response.xpath("//div[@class='title-and-desc']")
        items = []
        for site in sites:
            item = ScrapydemoItem()
            item['title'] = site.xpath("a/div/text()").extract()
            item['link'] = site.xpath("a/@href").extract()
            item['desc'] = site.xpath("div/text()").extract()
            items.append(item)
        return items
