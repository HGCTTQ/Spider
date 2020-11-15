#-*- codeing = utf-8 -*-
#@time : 2020/11/15 10:31
#@Author : 庚辰
#@File : 4.xpath解析案例-58二手房.py
#@Software : PyCharm
import requests
from lxml import etree
if __name__ == '__main__':
    #爬取页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是li标签对象
    li_list =tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        #局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')



