'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
import requests


def is_ip_valid(proxies):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    try:
        r = requests.get('https://www.youlu.net/classify/2-0106-1802-1.html', headers=headers, proxies=proxies, timeout=5)
    except:
        print('NO')
    else:
        print('YES')
# proxies = {"http": "http://124.200.36.118:40188"}
# proxies = {"http": "http://116.196.85.150:3128"}
# proxies = {"http": "http://39.137.69.9:80"}
# proxies = {"http": "http://112.253.11.113:8000"}
# proxies = {"http": "http://39.137.69.9:80"}
# proxies = {"http": "http://221.2.175.238:8060"}
# proxies = {"http": "http://113.161.116.90:8080"}
# proxies = {"http": "http://114.104.143.48:9999"}
# proxies = {"http": "http://110.243.20.23:9999"}
# proxies = {"http": "http://115.221.244.42:9999"}
# proxies = {"http": "http://123.56.118.36:8080"}
proxies = {"http": "http://115.29.199.16:8118"}




is_ip_valid(proxies)