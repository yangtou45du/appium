#!/usr/bin/env python
# -*- coding: cp936 -*-
from pyocr import pyocr
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.register import register
from tools.write_log import write_log
import time
from tools.myTools import *
from termcolor import *
from testCase.Login import Login
class Register():
    def __init__(self):
        pass
    def registerSuc(self,dict,assert_it):
        self.driver = register().registed(dict)

        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.NAME, u"完善信息")))
        result = self.driver.find_element_by_name(u"完善信息").text  # 完善信息
        # print result
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if result in assert_it:
            # write_log('\n' + nowTime + " login sucessful" + '\n')
            write_log(colored(('\n' + nowTime + " login sucessful" + '\n'), "red"))
            print  colored(('\n' + nowTime + " login sucessful" + '\n'), "green")
        else:
            write_log(colored(('\n' + nowTime + " login fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " login fail" + '\n'), "red")

        '''
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
           
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tv_result')))
        result = self.driver.find_element_by_id("com.vcolco.undunion:id/tv_result").text
        print result
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if result in assert_it:
            write_log('\n' + nowTime + " reidentified sucessful" + '\n')
            # print '\n' + nowTime + " reidentified sucessful" + '\n'
            print  colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "green")

        else:
            write_log(colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "red"))
            print colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "red")
            '''
        self.driver.quit()
#dict={"phone":"14875145875","password":"123456"}
#f=Register()
#f.registerSuc(dict,u"审核中")
