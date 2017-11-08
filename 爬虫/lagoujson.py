import urllib.request
import json
import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

html = response.read()
#把json形式的字符串转换为python形式的Unicode字符串
unicodestr = json.loads(html)

city_list = jsonpath.jsonpath(unicodestr, "$..name")

for item in city_list:
    print(item)

#禁用ascii编码格式，返回Unicode字符串
array = json.dumps(city_list, ensure_ascii=False)

with open("lagoucity.json", "w") as f:
    f.write(array)