#-*- codeing = utf-8 -*-
#@time : 2020/11/15 11:37
#@Author : 庚辰
#@File : 5.xpath解析案例-4k图片解析爬取.py
#@Software : PyCharm
import requests
from lxml import etree
import os
if __name__ == '__main__':
    #爬取页面源码数据
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    # response =requests.get(url=url,headers=headers)
    # #手动设定响应数据的编码格式
    # # response.encoding = 'utf-8'
    # page_text = response.text
    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for pageNum in range(1,16):
        #对应页码的url
        new_url = format(url%pageNum)

        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

    #数据解析：src的属性值  alt属性
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')

        for li in li_list:
            img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            #通用处理中文乱码的解决方案
            img_name = img_name.encode('iso-8859-1').decode('gbk')

            # print(img_name,img_src)
            #请求图片进行持久化存储
            img_data = requests.get(url=img_src,headers=headers).content
            img_path = 'picLibs/'+img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！！！')



