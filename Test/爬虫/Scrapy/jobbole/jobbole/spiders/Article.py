import scrapy
import urllib
import re
import datetime
from jobbole.items import JobboleItem
from jobbole.utils.common import get_md5


class ArticleSpider(scrapy.Spider):
    name = "Article"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']
    
    def parse(self, response):
        #获取列表中所有url
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            #这里通过meta参数将图片的url传递进来，这里用parse.urljoin的好处是如果有域名我前面的response.url不生效
            # 如果没有就会把response.url和post_url做拼接
            yield scrapy.http.Request(
                url=urllib.parse.urljoin(response.url, post_url),
                meta={
                    "front_image_url":
                    urllib.parse.urljoin(response.url, image_url)
                },
                callback=self.parse_detail)
        next_url = response.css(
            ".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield scrapy.http.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        article_item = JobboleItem()
        #文章封面图地址
        front_image_url = response.meta.get("front_image_url", "")
        title = response.xpath(
            '//div[@class="entry-header"]/h1/text()').extract_first()
        create_date = response.xpath(
            '//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[
                0].strip().split()[0]

        tag_list = response.xpath(
            '//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [
            element for element in tag_list
            if not element.strip().endswith("评论")
        ]
        tag = ",".join(tag_list)
        praise_nums = response.xpath(
            '//span[contains(@class,"vote-post-up")]/h10/text()').extract()
        if len(praise_nums) == 0:
            praise_nums = 0
        else:
            praise_nums = int(praise_nums[0])
        fav_nums = response.xpath(
            '//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0
        comment_nums = response.xpath(
            "//a[@href='#article-comment']/span/text()").extract()[0]
        match_com = re.match(".*(\d+).*", comment_nums)
        if match_com:
            comment_nums = int(match_com.group(1))
        else:
            comment_nums = 0

        content = response.xpath('//div[@class="entry"]').extract()[0]

        article_item["url_object_id"] = get_md5(response.url)  #这里对地址进行了md5变成定长
        article_item["title"] = title
        article_item["url"] = response.url
        try:
            create_date = datetime.datetime.strptime(create_date,
                                                     '%Y/%m/%d').date()
        except Exception as e:
            create_date = datetime.datetime.now().date()

        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = int(praise_nums)
        article_item["fav_nums"] = fav_nums
        article_item["comment_nums"] = comment_nums
        article_item["tag"] = tag
        article_item['content'] = content

        yield article_item