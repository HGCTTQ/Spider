#-*- codeing = utf-8 -*-
#@time : 2020/11/10 16:02
#@Author : 庚辰
#@File : zuifan.py
#@Software : PyCharm

#-*- codeing = utf-8 -*-
#@time : 2020/11/10 10:39
#@Author : 庚辰
#@File : pcbilibili.py
#@Software : PyCharm


from bs4 import BeautifulSoup         #网页解析，获取数据
import re                             #正则表达式，进行文字匹配
import urllib.request,urllib.error    #定制URL·获取网页数据
import xlwt                           #进行excel操作
import sqlite3                        #进行SQLite数据库操作
import gzip
from io import BytesIO




def main():
    baseurl = "https://www.bilibili.com/anime/index/#st=1&order=3&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page=1"
    #1.爬取网页
    datalist =getData(baseurl)

    # # savepath = ".\\豆瓣电影Top250.xls"
    # dbpath = "movie.db"
    # #3.保存数据
    # # saveData(datalist,savepath)
    # saveDate2DB(datalist,dbpath)
    # #askURL("https://movie.douban.com/top250?start=")


#影片详情链接的规则
# findLink = re.compile(r'<a href="(.*?)">')        #创建正则表达式对象，表示规则（字符串的模式）
# findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
# findInq = re.compile(r'<span class="inq">(.*)</span>')
# findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


findname = re.compile(r'class="bangumi-title">(.*?)</a>')
# findtype = re.compile(r'<span class="media-tag">(.*?)</span>')
# findlike = re.compile(r'<span class="media-info-intro-text">(.*?)</span>',re.S)


#爬取网页
def getData(baseurl):
    datalist = []

    url = baseurl
    html = askURL(url)         #保存获取到的网页源码

    # class ="bangumi-list clearfix"

    # 2.逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all("ul",class_ = "bangumi-list clearfix"):         #查找符合要求的字符串，形成列表
        print(item)    #测试查看电影item全部信息
        data = []      #保存一部电影的所有信息<span class="media-info-title-t">
        item = str(item)

        #影片详情链接
        # name = re.findall(findname,item)    #re库用来通过正则表达式查找指定的字符串
        # data.append(name)
        # print(name)
        # type = re.findall(findtype,item)
        # data.append(type)
        # print(type)
        # like = re.findall(findlike,item)
        # data.append(like)
        # print(like)
#得到一个指定一个URL的网页内容
def askURL(url):
    head = {             #模拟浏览器头部信息，向豆瓣服务器发送消息
        'Accept-Encoding':r'gzip,deflate',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
          #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode("utf-8")

        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



if __name__ =="__main__":    #当程宇执行时
#调用函数
    main()
    # init_db("movietext.db")
    print("爬取完毕")











