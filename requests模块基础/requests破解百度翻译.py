#-*- codeing = utf-8 -*-
#@time : 2020/11/12 21:37
#@Author : 庚辰
#@File : requests破解百度翻译.py
#@Software : PyCharm


import requests
import json

if __name__ == "__main__":
    #1指定url
    post_url = 'https://fanyi.baidu.com/sug'    #netework XHR请求   post请求 携带了参数 响应数据是一组json数据（content-type）
    #2进行ua伪装
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    #3post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #4请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5获取相应数据：json()方法返回的是obj（如果确认响应数据是json类型，才可以使用json()
    dic_obj = response.json()
    print(dic_obj)

    #6持久化存储
    fileName = word +'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!!')
