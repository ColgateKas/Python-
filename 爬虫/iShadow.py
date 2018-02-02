import requests
from lxml import etree

diggMax = 20


def url_open():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    }
    url = "https://global.ishadowx.net"
    response = requests.get(url, headers=headers)
    return response.content

def main():
    print('正在解析内容......')
    html = url_open().decode('utf-8')
    #响应返回的是字符串，解析为HTML DOM对象
    text = etree.HTML(html)
    node_list = text.xpath('//div[@class="col-sm-6 col-md-4 col-lg-4 us isotope-item"]')

    # liTemp = '' 
    # for pNumber in range(1, 201):



    #     for node in node_list:
    #         #推荐数
    #         digg = node.xpath('.//span[contains(@id,"digg_count")]')[0].text
    #         #标题
    #         title = node.xpath('.//a[@class="titlelnk"]')[0].text
    #         #链接
    #         link = node.xpath('.//a[@class="titlelnk"]//@href')[0]
    #         if (int(digg) >= diggMax):
    #             liTemp += '<li>推荐数：' + digg + '    <a href=' + link + ' target="_blank">' + title + '</a></li>' + '\n'


if __name__ == "__main__":
    main()
    print('全部解析完成')