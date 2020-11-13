#-*- codeing = utf-8 -*-
#@time : 2020/11/13 10:58
#@Author : 庚辰
#@File : requests药监总局.py
#@Software : PyCharm
                       #动态加载数据
                       # 在首页中对应的企业信息是通过ajax动态请求到的。
                       #通过对详情页url的观察发现：
                         #url的域名都是一样的，只有携带的参数（id）不一样
                         #id值可以从首页对应的ajax请求到的json串中获取
                         #域名和id值拼接成一个完整的企业对应的详情页的url
                       #详情页的企业信息数据是通过ajax动态请求到的。
                         #观察后发现：
                           #所有的post请求的url都是一样的，只有参数id值是不同的。
                           #如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url
import requests
import json
if __name__ =="__main__":
    #批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.111Safari / 537.36"
    }
    id_list = []  # 存储企业id
    all_data_list = []  # 存取所有企业的详情数据
    #参数的封装
    for page in range(1,16):
        page=str(page)
        data = {
            'on': 'true',
            'page': 'page',
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        json_ids = requests.post(url=url,headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        # print(id_list)

    #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        print(detail_json,'------------------ending-------------------')
        all_data_list.append(detail_json)

    #持久化存储 all data list
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')
    # with open('./huazhuangpin.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
