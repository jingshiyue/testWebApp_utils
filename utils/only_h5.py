#coding:utf-8
"""
测试纯H5，通过手机谷歌浏览器，登陆url. 
注意driver 要匹配手机谷歌浏览器版本
"""
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os
url='https://baidu.com'
desired_caps = {'platformName': 'Android',
                'deviceName': '127.0.0.1:21503',
                'platformVersion': '5.1.1',
                'noReset': True,
                'browserName':'Chrome'
                }


#desired_caps['platformName']='Android'
#desired_caps['platformVersion']='5.1.1'
#desired_caps['deviceName']='127.0.0.1:21503'

#desired_caps['app']=r'c:\Users\Mir-Z\Desktop\my\h5\dr.fone3.2.0.apk'
#desired_caps['appPackage']='com.wondershare.drfone'
#desired_caps['browserName']='Chrome'



driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print('浏览器启动成功')
driver.get(url)
time.sleep(15)
print(driver.contexts)
driver.switch_to.context('NATIVE_APP')
print('切换到原始APP成功')
try:
    WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//*[@text="否"]')).click()
    print('翻译提示已出现')
except:
    print('翻译提示未出现')
driver.switch_to.context('CHROMIUM')
print('切换到CHROMIUM成功')
WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('//*[@id="m-tabs-0-0"]/span/div/span')).click()
print('点击拨号盘成功')
#WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('xxxxx')).click()print('拨打按钮点击成功')
