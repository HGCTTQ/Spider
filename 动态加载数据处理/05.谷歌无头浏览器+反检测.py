#-*- codeing = utf-8 -*-
#@time : 2020/11/19 19:25
#@Author : 庚辰
#@File : 05.谷歌无头浏览器+反检测.py
#@Software : PyCharm

from selenium import webdriver
from time import sleep
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
# #实现规避检测
# from selenium.webdriver import ChromeOptions

# driver = webdriver.Chrome()
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# #实现规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])

#如何实现让selenium规避被检测到的风险
bro = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
#无可视化界面 (无头浏览器)  phantomJs
bro.get('https://www.baidu.com')

print(bro.page_source)

sleep(2)
bro.quit()

