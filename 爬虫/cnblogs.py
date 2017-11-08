import requests
from lxml import etree

diggMax = 20


def url_open(page):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    }
    if page == 1:
        url = "https://www.cnblogs.com"
        response = requests.get(url, headers=headers)
        return response.content
    else:
        data = {
            "CategoryType": "SiteHome",
            "ParentCategoryId": 0,
            "CategoryId": 808,
            "PageIndex": page,
            "TotalPostCount": 4000,
            "ItemListActionName": "PostList"
        }
        url = "https://www.cnblogs.com/mvc/AggSite/PostList.aspx"
        response = requests.post(url, headers=headers, data=data)
        return response.content


def saveHtml(content):
    html = '\
    <html>\
    <head>\
        <title>cnblogs</title>\
    </head>\
    <body>\
        <ul>' + content + '</ul>\
    </body>\
    </html>'

    with open('cnblogs.html', 'w') as f:
        f.write(html)


def main():
    liTemp = '' 
    for pNumber in range(1, 201):
        print('正在解析第%s页......' % pNumber)
        html = url_open(pNumber).decode('utf-8')

        #响应返回的是字符串，解析为HTML DOM对象
        text = etree.HTML(html)

        node_list = text.xpath('//div[@class="post_item"]')

        for node in node_list:
            #推荐数
            digg = node.xpath('.//span[contains(@id,"digg_count")]')[0].text
            #标题
            title = node.xpath('.//a[@class="titlelnk"]')[0].text
            #链接
            link = node.xpath('.//a[@class="titlelnk"]//@href')[0]
            if (int(digg) >= diggMax):
                liTemp += '<li>推荐数：' + digg + '    <a href=' + link + ' target="_blank">' + title + '</a></li>' + '\n'
    saveHtml(liTemp)


if __name__ == "__main__":
    main()
    print('全部解析完成')