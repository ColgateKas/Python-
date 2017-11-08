from bs4 import BeautifulSoup
import requests
import time


def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)
    text = input("请输入验证码：")
    return text


def login():
    sess = requests.Session()
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    captcha_url = "http://guahao.zjol.com.cn/validate_Code/login?%d" % (time.time())
    captcha_data = sess.get(captcha_url, headers=headers).content
    text = captcha(captcha_data)

    data = {
        "idcard" : "330381200002298224",
        "password" : "0843ee326a2831b0d1dcae5c60e6e374",
        "verifyCode" : text
    }
    response =sess.post("http://guahao.zjol.com.cn/logon", data = data, headers = headers)
    #print(response.text)

    response = sess.get("http://guahao.zjol.com.cn/member/orderList", headers = headers)
    print(response.text)

if __name__ =="__main__":
    login()
