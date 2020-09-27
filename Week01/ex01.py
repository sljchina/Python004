import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
from time import sleep

# 定义代理列表
USER_AGENT_LIST=[
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

import random

# 随机选择一个代理
user_agent = random.choice(USER_AGENT_LIST)

# user_agent = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

# 产生头文件
header = {'user-agent':user_agent}
# 存储电影信息的数组
film_infos = []
# 目标链接
myurl = 'https://maoyan.com/films?showType=3'
# 网站主域名
main_url = 'https://maoyan.com'
# 访问目标链接
response = requests.get(myurl,headers=header)
# 获得网页文本
bs_info = bs(response.text, 'html.parser')

# print(response.text)
# print(f'返回码是:{response.status_code}')
#app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(2) > div.channel-detail.movie-item-title
# 创建电影列表，用于存储目标电影的链接
film_list = []

for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    # print(tags)
    for atag in tags.find_all('a',):
        # 获得链接
        film_list.append(main_url+atag.get('href'))



for i in range(0,10):
    url = film_list[i]
    # print(url)
    # 访问目标链接
    response = requests.get(url,headers=header)
    # 获得网页文本
    bs_info = bs(response.text, 'html.parser')
# body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container
    for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        for name in tags.find_all('h1', attrs={'class': 'name'}):
            film_name = name.text
            print(film_name)
# body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container > ul > li:nth-child(1)
        atag = tags.find_all('li', attrs={'class': 'ellipsis'})
        categorys = atag[0].find_all('a')
        film_categorys = []
        for category in categorys:
            print(category.text)
            film_categorys.append(category.text)
        film_date = atag[2].text
        print(film_date)
        film_info = [film_name, film_categorys,film_date]
        film_infos.append(film_info)



    # selector = lxml.etree.HTML(response.text)

    # film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    # print(film_name)
    # film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')
    # print(film_type)
    # film_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    # print(film_date)

    sleep(1)


import pandas as pd

movie = pd.DataFrame(data = film_infos)

movie.to_csv('movie.csv', encoding='UTF-8', index=False, header=False)

