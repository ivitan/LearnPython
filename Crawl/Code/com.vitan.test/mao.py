#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-28 上午11:51
# @Author  : Vitan
# @File    : mao.py

import requests
import re
import json
from multiprocessing import Pool
from requests.exceptions import RequestException

def get_one_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            html = response.text
            return html
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
    + '.*?<p.*?title="(.*?)".*?</p>.*?star">(.*?)</p>'
    + '.*?releasetime">(.*?)</p>.*?integer">(.*?)'
    + '<.*?fraction">(.*?)</i>',re.S)
    movies = re.findall(pattern,html)
    for item in movies:
        yield{
            '排名':item[0],
            '电影名':item[1],
            '主演':item[2].strip()[3:],
            '上映时间':item[3][5:],
            '评分':item[4]+item[5]
        }

def write_to_txt(content):
    # 采用 append 追加模式，字符集为utf8
    with open('movies.txt','a',encoding='utf8') as f:
        # 采用json的dumps方法来初始化字符串
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_txt(item)

if __name__ == '__main__':
    pool = Pool() # 多线程
    pool.map(main, [i*10 for i in range(10)])
    pool.close()
    pool.join()