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
    url = 'https://www.vmgirls.com/15071.html'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    response =requests.get(url=url,headers=headers)
    #手动设定响应数据的编码格式
    # response.encoding = 'utf-8'
    page_text = response.text

    #数据解析：src的属性值  alt属性
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/ html / body / main / div / div[2] / div[1] / div / div[4] / div[3] / a')
    # print(li_list)
    # / html / body / main / div / div[2] / div[1] / div / div[4] / div[3] / a[2] / img
    # / html / body / main / div / div[2] / div[1] / div / div[4] / div[3]

    #创建一个文件夹
    if not os.path.exists('./vmgirlsLibs2'):
        os.mkdir('./vmgirlsLibs2')

    for li in li_list[1:]:

        img_src = 'https:'+li.xpath('./@href')[0]
        img_name = img_src.split('/')[-1]+'.jpg'

        # 通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        print(img_name,img_src)
        #请求图片进行持久化存储
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'vmgirlsLibs2/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')



