#-*- codeing = utf-8 -*-
#@time : 2020/11/15 17:15
#@Author : 庚辰
#@File : 8.xpath解析案例-全国城市名称爬取.py
#@Software : PyCharm
import requests
from lxml import etree
#项目需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
# if __name__ == '__main__':
#     #爬取页面源码数据
#     url = 'https://www.aqistudy.cn/historydata/'
#     headers = {
#         "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
#     }
#     page_text = requests.get(url=url,headers=headers).text
#     tree = etree.HTML(page_text)
#     host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
#     all_city_names =[]
#     #解析到了热门城市
#     for li in host_li_list:
#         hot_city_name = li.xpath('./a/text()')[0]
#         all_city_names.append(hot_city_name)
#
#     #解析的是全部城市的名称
#     city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
#     for li in city_name_list:
#         city_name = li.xpath('./a/text()')[0]
#         all_city_names.append(city_name)
#
#     print(all_city_names,len(all_city_names))



if __name__ == '__main__':
    #爬取页面源码数据
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    #解析到了热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a
    # //div[@class="bottom"]/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names =[]
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)

    print(all_city_names,len(all_city_names))