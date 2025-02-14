from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException,NoSuchElementException,TimeoutException
from pyquery.pyquery import PyQuery as pq
import pymongo
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

client = pymongo.MongoClient('localhost')
db = client['Qunar']

def lastPage():
    try:
        url = 'http://piao.qunar.com/ticket/list_%E6%88%90%E9%83%BD.html?keyword=%E6%88%90%E9%83%BD&page=1#from=home_remen&in_track=qunar_djmp_gnmdd_%E6%88%90%E9%83%BD'
        driver.get(url)
        doc = pq(driver.page_source)
        doc = str(doc.find('.pager'))
        pattern = re.compile('<div.*?<a.*?data-pager-pageno="63">(\d+)</a>', re.S)
        result = re.match(pattern, doc)
        total = int(result.group(1))
        print(total)
        return total
    except TimeoutException:
        return total

def get_url():
    doc = pq(driver.page_source)
    doc = doc.find('.sight_item_caption')
    li = []
    for box in doc.items():
        url = 'http://piao.qunar.com'+str(box.find('.name').attr('href'))
        li.append(url)
    return li

def get_comment_last():
    # 评论总页数
    doc = pq(driver.page_source)
    doc = doc.find('#pageContainer')
    li = [i.text() for i in doc.find('.mp-pager-item').items()]
    return int(li[-2])

def get_comment_next(i):
    try:
        next = driver.find_element_by_css_selector('.mp-pager-next.mp-pager-item')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mp-pager-next.mp-pager-item')))
        next.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.pager em'),str(i)))
    except TimeoutException:
        get_comment_next(i)
    except WebDriverException:
        get_comment_next(i)

def get_page_comments():
    doc = pq(driver.page_source)
    doc = doc.find('.mp-comments-list')
    for item in doc.find('.mp-comments-item').items():
        usr = item.find('.mp-comments-username').text()
        date = item.find('.mp-comments-time').text()
        comment = item.find('.mp-comments-desc').text()
        view = {
            'user':usr,
            'date':date,
            'comment':comment
        }
        print(view)
        # save_to_mongo(view)

def get_all_url():
    # 所有景点 Url
    driver.execute_script('window.open()')  # 打开新的选项卡
    driver.switch_to.window(driver.window_handles[1])
    total = lastPage()
    driver.switch_to.window(driver.window_handles[0])
    all_url = []
    for i in range(1, total - 60):
        url = 'http://piao.qunar.com/ticket/list_%E6%88%90%E9%83%BD.html?keyword=%E6%88%90%E9%83%BD&page=' + str(
            i) + '#from=home_remen&in_track=qunar_djmp_gnmdd_%E6%88%90%E9%83%BD'
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next')))
        all_url.extend(get_url())
        print(all_url)
    return all_url

def get_allcomment_url():
    all_url = get_all_url()
    # 景点所有评论
    for url in all_url:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mp-pager-next.mp-pager-item')))
        total = get_comment_last()  # 评论页数
        get_page_comments()
        print(total)
        for i in range(2, total + 1):
            get_comment_next(i)
            get_page_comments()

def save_to_mongo(view):
    if db['comment'].insert_one(view):
        print('Saving to MongoDB',view)
        return True
    return False

def main():
    get_allcomment_url()
    get_page_comments()

if __name__ == '__main__':
    main()