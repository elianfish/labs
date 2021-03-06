#coding=utf-8

###########################################################
# 作者: ooobj
# 时间: 2014-12-26
# 博客：http://www.cnblogs.com/ooobj/
# 运行环境：python3, requests-2.2.1, beautifulsoup-4.1.3
# 说明：新浪sina.cn邮箱注册机，仅供学习，请勿由于商业用途
#
###########################################################
import time
import json
import random
import string
import requests
from bs4 import BeautifulSoup


s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.35'
s.headers['Referer'] = 'https://mail.sina.com.cn/register/regmail.php'
#s.proxies = {"http": "http://127.0.0.1:8888"}

for i in range(0, 3):
    reg_url = 'https://mail.sina.com.cn/register/regmail.php'
    r = s.get(reg_url, verify=False)
    soup = BeautifulSoup(r.text)
    form = soup.find('form', {'name': 'frm_reg_alp'})
    extcode = form.find('input', {'name': 'extcode'})['value']
    swfimgsk = form.find('input', {'name': 'swfimgsk'})['value']
    forbin = form.find('input', {'name': 'forbin'})['value']

    imgurl = 'https://mail.sina.com.cn/cgi-bin/imgcode.php?t=%d' % int(time.time())
    r = s.get(imgurl, verify=False)
    with open('cap.png', 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    code = input('code: ')
    url = 'https://mail.sina.com.cn/register/regmail.php'
    username = (''.join(random.sample(string.ascii_lowercase, 12))) + (''.join(random.sample(string.digits, 4)))
    password = (''.join(random.sample(string.ascii_lowercase, 4))) + (''.join(random.sample(string.digits, 4)))
    data = {
        'act': '1',
        'agreement': 'on',
        'email': username+'@sina.cn',
        'psw': password,
        'imgvcode': code,
        'showcode': 'imgCodeEN',
        'swfimgsk': swfimgsk,
        'forbin': forbin,
        'extcode': extcode,
        'r': ''
        }

    r = s.post(url, data=data, verify=False)
    rj = json.loads(r.text)
    if rj['errno'] != 0:
        print(rj['msg'])
    else:
        print('注册成功！')
        print(username, password)

