#!/user/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from lxml import etree
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

cookie = ''
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


def login():
    global cookie
    url = "https://qianbai.ml/auth/login"
    loginp = {
        'email': '351883791@qq.com',
        'passwd': 'missxiaohuang',
        'remember_me': 'week'
    }
    try:
        response = requests.post(url, data=loginp, headers=headers)
        cookie = response.cookies
        ret = response.json()['ret']
        if ret == 0:
            return 'err'
        else:
            return 'success'
    except:
        sendEmail('登录异常，请检查！')
        return 'err'


def main():
    global cookie
    print('爬虫初始化......')
    rcode = login()
    if rcode == 'success':
        try:
            response = requests.post(
                "https://qianbai.ml/user/checkin", cookies=cookie)
            msg = response.json()['msg']

            response = requests.get(
                "https://qianbai.ml/", headers=headers, cookies=cookie)
            html = response.content.decode()
            dom = etree.HTML(html)
            node_list = dom.xpath('//div[@class="inner"]//code')
            emailHtml = '<html><body>'
            emailHtml += "<p>用户：" + node_list[0].text + "</p>"
            emailHtml += "<p>等级：" + node_list[1].text + "</p>"
            emailHtml += "<p>过期时间：" + node_list[2].text + "</p>"
            emailHtml += "<p>总流量：" + node_list[3].text + "</p>"
            emailHtml += "<p>已用流量：" + node_list[4].text + "</p>"
            emailHtml += "<p>剩余流量：" + node_list[5].text + "</p>"
            emailHtml += "<p>今日签到 " + msg + "</p>"
            emailHtml += '</body></html>' ''
            sendEmail(emailHtml)
            print("用户：" + node_list[0].text)
            print("等级：" + node_list[1].text)
            print("过期时间：" + node_list[2].text)
            print("总流量：" + node_list[3].text)
            print("已用流量：" + node_list[4].text)
            print("剩余流量：" + node_list[5].text)
            print("今日签到 " + msg)
            print("恭喜流量自动签到完成！")
        except Exception:
            sendEmail('流量签到异常，请检查！')
    else:
        print('登录失败！')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendEmail(content):
    from_addr = "351883791@qq.com"
    password = "lmdlibwwpekgbhfd"
    to_addr = "245359946@qq.com"
    smtp_server = "smtp.qq.com"
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = _format_addr('流量自动签到提醒 <%s>' % from_addr)
    msg['To'] = _format_addr('Python爬虫 <%s>' % to_addr)
    msg['Subject'] = Header('代理流量自动签到提醒', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == "__main__":
    main()