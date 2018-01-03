#!/usr/bin/env python
# -*- coding: cp936 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.reIdentified import reIdentified
from tools.write_log import write_log
from common.login import login
import time
from termcolor import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tools.myTools import *
class ReIdendified():
    def __init__(self):
        pass
    def submit_suc(self,dict,assert_it):
        self.driver=reIdentified().reIdentifing(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tv_result')))
        result=self.driver.find_element_by_id("com.vcolco.undunion:id/tv_result").text
        print result
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if result in assert_it:
            write_log('\n' + nowTime + " reidentified sucessful" + '\n')
            #print '\n' + nowTime + " reidentified sucessful" + '\n'
            print  colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "green")

        else:
            write_log(colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "red"))
            print colored(('\n' + nowTime + " reidentified sucessful" + '\n'), "red")


        self.driver.quit()


#dict={"phone":"13730687504","password":"123456"}
#f=ReIdendified()
#f.submit_suc(dict,u"审核中")
