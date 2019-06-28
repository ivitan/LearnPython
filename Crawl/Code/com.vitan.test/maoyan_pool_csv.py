#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-28 下午12:07
# @Author  : Vitan
# @File    : maoyan_pool_csv.py
import requests
import re
import pandas
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
    pageary = []
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
    + '.*?<p.*?title="(.*?)".*?</p>.*?star">(.*?)</p>'
    + '.*?releasetime">(.*?)</p>.*?integer">(.*?)'
    + '<.*?fraction">(.*?)</i>',re.S)
    movies = re.findall(pattern,html)
    for item in movies:
        dict = {
            '排名':item[0],
            '电影名':item[1],
            '主演':item[2].strip()[3:],
            '上映时间':item[3][5:],
            '评分':item[4]+item[5]
        }
        pageary.append(dict)
    return pageary

def write_to_csv(pageary):
    ary = []
    ary = ary + pageary
    df = pandas.DataFrame(ary)
    df.to_csv('movies.csv')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    ary = parse_one_page(url)
    write_to_csv(ary)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
    pool.close()
    pool.join()