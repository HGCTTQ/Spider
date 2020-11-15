#-*- codeing = utf-8 -*-
#@time : 2020/11/14 11:20
#@Author : 庚辰
#@File : 0.爬取图片.py
#@Software : PyCharm
import requests
if __name__ =="__main__":
    #如何爬取图片数据
    url = 'http://pic.netbian.com/uploads/allimg/201113/001926-160519796603e7.jpg'
    #content返回的是二进制形式的图片数据
    #text(字符串)  content(二进制)  json() (对象)
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)


