import urllib.request
import urllib.error
import random

url = 'http://www.whatismyip.com.tw/'

iplist = ["181.113.116.134:63909","192.129.199.175:9001","183.237.206.92:53281","121.69.76.154:8118","101.81.183.236:53281"]

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [(
    'User-Agent',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
)]

urllib.request.install_opener(opener)

try:
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print(e.reason)
except ConnectionAbortedError as e:
    print(e.reason)
