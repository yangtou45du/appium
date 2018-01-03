#!/usr/bin/env python
# -*- coding: cp936 -*-
from appium import webdriver
from time import sleep
class openApp():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'honor-ATH-CL00-WCH7N15B05009491'
        desired_caps['appPackage'] = 'com.vcolco.undunion'
        desired_caps['appActivity'] = 'com.vcolco.undunion.SplashActivity'
        desired_caps['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #self.driver.find_element_by_name(u"连接城际专线").click()  # open app










