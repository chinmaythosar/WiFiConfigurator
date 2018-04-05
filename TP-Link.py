from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

usernameStr = 'admin'
passwordStr = 'admin'
ssidStr = 'YourWiFiName'
pskStr = 'YourWiFiPassword'
channelNumber = 1 #Replace this with either 1 or 6 or 11 for selecting the channel

browser = webdriver.Chrome()
browser.get(('http://192.168.0.1'))

#Fill Username
username = browser.find_element_by_id('userName')
username.send_keys(usernameStr)

#FillPassword
password = browser.find_element_by_id('pcPassword')
password.send_keys(passwordStr)


#ButtonClick

browser.find_element_by_id('loginBtn').click()
browser.implicitly_wait(2)


#Switch to Wireless Settings
browser.switch_to_frame('bottomLeftFrame')
browser.find_element_by_id('menu_wl').click()
browser.implicitly_wait(2)


#Change SSID
browser.switch_to_default_content()
browser.switch_to_frame('frame2')

browser.find_element_by_id('ssid').clear()
ssid = browser.find_element_by_id('ssid')
ssid.send_keys(ssidStr)

#Select Channel

selectC = Select(browser.find_element_by_id('channel'))
selectC.select_by_index(channelNumber)

#Select ChannelWidth to 20MHz

selectCW = Select(browser.find_element_by_id('bandWidth'))
selectCW.select_by_value('20M')

browser.find_element_by_id('tail').click()

time.sleep(8)


#Change WPA2 Passcode
browser.switch_to_default_content()
browser.switch_to_frame('frame1')
browser.find_element_by_id('menu_wlsec').click()

browser.switch_to_default_content()
browser.switch_to_frame('frame2')

browser.find_element_by_id('pskSecret').clear()
psk = browser.find_element_by_id('pskSecret')
psk.send_keys(pskStr)
browser.find_element_by_id('tail').click()

time.sleep(10)


browser.switch_to_default_content()
browser.switch_to_frame('frame1')
browser.find_element_by_id('menu_logout').click()
browser.implicitly_wait(2)
time.sleep(2)
#browser.quit()

alert = browser.switch_to_alert()
alert.accept()
browser.implicitly_wait(2)
time.sleep(2)

browser.quit()

