import urllib.request
import json
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/2/"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
request = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(request).read()

#响应返回的是字符串，解析为HTML DOM对象
text = etree.HTML(html)

node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')

for node in node_list:
    #用户名
    username = node.xpath('.//h2')[0].text
    #图片链接
    image = node.xpath('.//div[@class="thumb"]//@src')
    #段子内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    #点赞
    zan = node.xpath('.//i')[0].text
    #评论
    comments = node.xpath('.//i')[1].text

    items = {
        "username": username,
        "image": image,
        "content": content,
        "zan": zan,
        "comments": comments
    }
    print(json.dumps(items, ensure_ascii=False))
    # with open('qiushi.json', 'a') as f:
    #     f.write(json.dumps(items, ensure_ascii=False) + '\n')
