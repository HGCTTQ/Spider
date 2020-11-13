#-*- codeing = utf-8 -*-
#@time : 2020/11/13 9:15
#@Author : 庚辰
#@File : requests网页采集器.py
#@Software : PyCharm

import requests
if __name__ == "__main__":
    #ua伪装：将对应的ua伪装到一个字典中
    headers ={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw     #query=搜索的内容
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    fileName = kw +'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')