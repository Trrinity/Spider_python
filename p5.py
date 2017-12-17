# -*- coding:utf8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_size(1080,800)
driver.implicitly_wait(10)

driver.get('https://exmail.qq.com/cgi-bin/bizmail?sid=y_jjEdONPtM2YEgR,2&t=biz_rf_home&init=1#mbr/list/8048531,true,false,false')


driver.find_element_by_name("").send_keys("")
