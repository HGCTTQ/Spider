#-*- codeing = utf-8 -*-
#@time : 2020/11/13 10:16
#@Author : 庚辰
#@File : requests豆瓣电影爬取.py
#@Software : PyCharm
import requests
import json
if __name__ =="__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '25',
        'interval_id': '100:90',
        'action':'',
        'start': '0', #从库中的第几部电影去取
        'limit': '20', #一次取出的个数
    }
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    response=requests.get(url=url,params=param,headers=headers)

    list_data = response.json()
    print(list_data)
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!!!')

