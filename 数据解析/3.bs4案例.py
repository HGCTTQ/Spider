#-*- codeing = utf-8 -*-
#@time : 2020/11/14 19:53
#@Author : 庚辰
#@File : 3.bs4案例.py
#@Software : PyCharm
from bs4 import BeautifulSoup
import requests
#需求: 爬取三国演义小说所有的章节标题和章节内容
if __name__ =="__main__":
    #对首页的页面数据进行爬取
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).text

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup =BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')