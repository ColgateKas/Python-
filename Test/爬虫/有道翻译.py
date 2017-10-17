# -*- coding:utf-8 -*-
# API key：273646050
# keyfrom：11pegasus11
import json
import sys
from urllib.parse import urlparse, quote, urlencode, unquote
from urllib.request import urlopen

def fetch(query_str = ''):
    query_str = query_str.strip("'").strip('"').strip()
    if not query_str:
        query_str = 'python'

    #print(query_str)
    query = {
        'q':query_str
    }
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + urlencode(query)
    response = urlopen(url, timeout=3)
    html = response.read().decode('utf-8')
    return html

def parse(html):
    d = json.loads(html)
    #print(d)
    try:
        if d.get('errorCode') == 0:
            explains = d.get('basic').get('explains')
            for i in explains:
                print(i)
        else:
            print('无法翻译')
    except:
        print('翻译出错，请输入合法单词')

def main():
    while 1:
        s = input("请输入要翻译的内容(输入Q退出)：")
        if s == 'Q':
            sys.exit(0)
        else:
            parse(fetch(s))
            print('\r')

if __name__=='__main__':
    main()
