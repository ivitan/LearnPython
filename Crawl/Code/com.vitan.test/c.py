#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-20 下午1:13
# @Author  : Vitan
# @File    : c.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from pyquery.pyquery import PyQuery as pq
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

# driver.get('http://piao.qunar.com/ticket/list_%E6%88%90%E9%83%BD.html#from=home_remen&in_track=qunar_djmp_gnmdd_%E6%88%90%E9%83%BD')
# doc = pq(driver.page_source)
# doc = doc.find('.pager')
# doc = str(doc)
# print(doc)
# print(type(doc))
# pattern = re.compile('<div.*?<a.*?data-pager-pageno="63">(\d+)</a>',re.S)
# result = re.match(pattern,doc)
# total = result.group(1)
# total = int(total)
# print(type(total))

# def place():
#     anchors = driver.find_elements_by_css_selector('.sight_item_caption a')
#     for a in anchors:
#         url = a.get_attribute('href')
#         return url
# pla

import time
from selenium import webdriver

#创建浏览器对象
browser = webdriver.Chrome()
#访问淘宝
browser.get('https://www.taobao.com')
#打开新的选项卡（执行js语句 execute_script（'window.open()')
browser.execute_script('window.open()')

#切换到第2个选项卡,下标为1
browser.switch_to.window(browser.window_handles[1])
#访问 百度
browser.get('https://www.baidu.com')
#休眠1s
time.sleep(1)
#切换到第1个选项卡，下标为0
browser.switch_to.window(browser.window_handles[0])
#访问百度
browser.get('https://www.vitan.me')