#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-25 下午6:48
# @Author  : Vitan
# @File    : dddc.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from pyquery.pyquery import PyQuery as pq
import time
import pymongo

broswer = webdriver.Chrome()
#Element is not currently visible and may not be manipulated"
# broswer.set_window_size(1920, 1080)
wait = WebDriverWait(broswer,10)

client = pymongo.MongoClient('localhost')
db = client['MaFengWoView']

def search_first(url):
    try:
        broswer.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pi.pg-last')))
        total = int(broswer.find_element_by_css_selector('.pi.pg-last').get_attribute('data-page'))
        print(total)
        place()
        return total
    except TimeoutException:
        return search_first(url)

def search_next(page):
    try:
        next = broswer.find_element_by_css_selector('.pi.pg-next')
        next.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.pg-current'), str(page)))
        time.sleep(2)
        place()
    except NoSuchAttributeException:
        search_next(page)

def place():
    anchors = broswer.find_elements_by_css_selector('.scenic-list.clearfix li a')
    for a in anchors:
        url = a.get_attribute('href')
        total = view_first(url)
        for page in range(2,total+1):
            view_next(page)

    # html = broswer.page_source
    # doc = pq(html)
    # anchors = doc('.scenic-list.clearfix li a')
    # for a in anchors.items():
    #     url = a.attr('href')
    #     print(url)

def view_first(url):
    try:
        broswer.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pi.pg-last')))
        total = int(broswer.find_element_by_css_selector('.pi.pg-last').get_attribute('data-page'))
        get_view()
        return total
    except TimeoutException:
        return view_first(url)

def view_next(page):
    try:
        next = broswer.find_element_by_css_selector('.pi.pg-next')
        broswer.implicitly_wait(2)

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.pg-current'),str(page)))
        get_view()
    except NoSuchAttributeException:
        view_next(page)

def get_view():
    html = broswer.page_source
    doc = pq(html)
    lis = doc('.rev-item.comment-item.clearfix')
    for li in lis.items():
        view = {
            'name':li.find('.name').text(),
            'level':li.find('.level').text(),
            'txt':li.find('.rev-txt').text()
        }
        save_to_mongo(view)

def save_to_mongo(view):
    if db['MaFengWoView'].insert_one(view):
        print('Saving to MongoDB',view)
        return True
    return False

def main():
    url = 'http://www.mafengwo.cn/jd/10088/gonglve.html'
    total = search_first(url)
    for page in range(2,total+1):
        search_next(page)
    #     print('Clicking',page,'页')
    # url = 'http://www.mafengwo.cn/poi/449.html'
    # total = view_first(url)
    # for page in range(2,total+1):
    #     view_next(page)

if __name__=='__main__':
    main()