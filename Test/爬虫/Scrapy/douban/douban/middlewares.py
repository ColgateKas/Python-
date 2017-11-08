# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from douban.settings import USER_AGENTS
from douban.settings import PROXIES
import base64


#生成随机User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            #没有代理验证的使用
            request.meta['proxy'] = 'http://' + proxy['ip_prot']
        else:
            #有代理验证的使用
            base64_userpwd = base64.b64encode(
                proxy['user_passwd'].encode(encoding="utf-8"))
            request.meta['proxy'] = 'http://' + proxy['ip_prot']
            request.headers['Proxy-Authorization'] = 'Basic ' + str(base64_userpwd)
