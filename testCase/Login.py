#!/usr/bin/env python
# -*- coding: cp936 -*-
from pyocr import pyocr
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.login import login
from tools.write_log import write_log
import time
from tools.myTools import *
from termcolor import *
class Login():
    def __init__(self):
        pass
    def loginByPasswordSuc(self,dict,assert_it):
        '''正确的手机号和密码'''
        self.driver=login().LoginByPassword(dict)

        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tvMoreTask')))
        result=self.driver.find_element_by_id("com.vcolco.undunion:id/tvMoreTask").text #查看任务列表
        #print result
        nowTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if result in assert_it:
            write_log('\n' + nowTime + " login sucessful" + '\n')
            #write_log(colored(('\n' + nowTime + " login sucessful" + '\n'), "red"))
            print  colored(('\n' + nowTime + " login sucessful" + '\n'), "green")
        else:
            write_log(colored(('\n' + nowTime + " login fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " login fail" + '\n'), "red")


        self.driver.quit()
    def loginByDynamicPasswordSuc(self,dict,assert_it):
        self.driver=login().loginByDynamicPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tvMoreTask')))
        result = self.driver.find_element_by_id("com.vcolco.undunion:id/tvMoreTask").text  # 查看任务列表
        # print result
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if result in assert_it:
            # write_log('\n' + nowTime + " login sucessful" + '\n')
            write_log(colored(('\n' + nowTime + " login sucessful" + '\n'), "red"))
            print  colored(('\n' + nowTime + " login sucessful" + '\n'), "green")
        else:
            write_log(colored(('\n' + nowTime + " login fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " login fail" + '\n'), "red")
        self.driver.quit()

#dict={"phone":"18782256120","password":"123456"}
#f=Login()
#f.loginByDynamicPasswordSuc(dict,u"查看任务列表")


