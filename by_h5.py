#coding:utf-8
"""
测试混合，driver.switch_to.context 来切换native 与 webview
注意driver 要匹配webview版本
"""
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='5.1.1'
desired_caps['deviceName']='127.0.0.1:21503'

desired_caps['app']=r'c:\Users\Mir-Z\Desktop\my\h5\dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)
contexts=driver.contexts
print(contexts)
print("-------------------")

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()  # native com.wondershare.drfone:id/btnBackup

WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()  #native com.wondershare.drfone:id/btnRecoverData

WebDriverWait(driver,30).until(lambda x:x.find_element_by_class_name('android.webkit.WebView')) #native android.webkit.WebView
contexts=driver.contexts
print(contexts)  #[u'NATIVE_APP', u'WEBVIEW_com.wondershare.drfone']
#WebView in com.wondershare.drfone
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
contexts=driver.contexts
print(contexts)

driver.find_element_by_id('email').send_keys('shuqing2018@163.com')  #webview <input type="email" id="email" placeholder="Input your Email address">
#//android.webkit.WebView[@content-desc="[OFFICIAL]dr.fone app - Backup and restore data on your mobile"]/android.view.View[8]/android.widget.EditText
driver.find_element_by_class_name('btn_send').click() #webview <button class="btn_send active" onclick="subEmail()">Submit</button>
#	//android.widget.Button[@content-desc="Submit"]

driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()