#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.changePassword import changePassword
from tools.write_log import write_log
from selenium.webdriver.common.by import By
import time
import sys
from tools.myTools import *
from termcolor import *
from common.login import login
class ChangePassword():
    def __init__(self):
        pass
    def changePasswordSuc(self,dict,assert_it):
        self.driver =changePassword().changePassword(dict)

        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tvMoreTask')))
        result=self.driver.find_element_by_id("com.vcolco.undunion:id/tvMoreTask").text #�鿴�����б�
        #print result
        nowTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if result in assert_it:
            write_log('\n' + nowTime + " change password sucessful" + '\n')
            #write_log(colored(('\n' + nowTime + " login sucessful" + '\n'), "red"))
            print  colored(('\n' + nowTime + " change password sucessful" + '\n'), "green")
        else:
            write_log(colored(('\n' + nowTime + " change password fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " change password fail" + '\n'), "red")


        self.driver.quit()

#dict={"phone":"18782256120","password":"123456"}
#f=ChangePassword()
#f.changePasswordSuc(dict,u"�鿴�����б�")