#-*- codeing = utf-8 -*-
#@time : 2020/11/19 17:47
#@Author : 庚辰
#@File : 04.模拟登陆QQ空间.py
#@Software : PyCharm

from selenium import webdriver
from time import sleep
#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('653251391')
sleep(1)
password_tag.send_keys('222')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)

bro.quit()