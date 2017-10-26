# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo


def get_detail_info(url, data=None):

    # 爬取单条租房信息（标题，图片，房东，日租金，房东性别，房东头像）
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    time.sleep(2)

    title = soup.select('h4 > em')[0].get_text()
    address = soup.select('span.pr5')[0].get_text()
    rent = soup.select('div.day_l > span')[0].get_text()
    image = soup.select('#curBigImage')[0].get('src')
    lorder_pic = soup.select('div.member_pic > a > img')[0].get('src')
    lorder_name = soup.select('a.lorder_name')[0].get_text()
    lorder_sex = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')[0].get('class')

    def get_gender(class_name):
        if class_name == "member_boy_ico":
            return  "男"
        else:
            return "女"

    data = {
        '标题': title,
        '地址': address,
        '日租金': rent,
        '图片': image,
        '房东头像': lorder_pic,
        '房东姓名': lorder_name,
        '房东性别': get_gender(lorder_sex)
    }
    print(data)
    return data

def get_all_data(urls):
    # 爬取所有租房信息
    all_data = []
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links = soup.select('#page_list > ul > li > a')
        for link in links:
            href = link.get('href')
            all_data.append(get_detail_info(href))
    return all_data

# 定义数据库
client = pymongo.MongoClient("mongodb://rhvhlogger:rhvhlogger@10.66.8.111:27017")
rent_info = client['rent_info1']  # 给数据库命名
sheet_table = rent_info['sheet_table1']  # 创建表单

urls = ['http://sh.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 2)]
# 3页的租房信息的链接
datas = get_all_data(urls)

for item in datas:
    # 将数据存入数据库
    sheet_table.insert_one(item)

# for item in sheet_table.find():
    # 筛选出日租金大于等于500的租房信息，并打印出来
#     if int(item['日租金']) >= 500:
#         print(item)