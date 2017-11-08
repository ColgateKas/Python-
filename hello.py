import socket
import urllib.request, http.cookiejar
import urllib.parse

url = 'http://httpbin.org/post'
dict = {'name': 'zhaofan'}

data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
print(data)
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

req = urllib.request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)')
req.add_header('Host', 'httpbin.org')

try:
    #response = urllib.request.urlopen(req, timeout=0.5)
    response = opener.open('http://www.baidu.com')
    #print(response.read().decode('utf-8'))
    for item in cookie:
        print(item.name + '=' + item.value)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')