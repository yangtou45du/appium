#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.createCar import createCar
from tools.write_log import write_log
from selenium.webdriver.common.by import By
import time
from termcolor import *
class CreateCar():
    def __init__(self):
        pass
    def createCar_suc(self,dict,assert_it):
        self.driver=createCar().createNewCar(dict)
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, "com.vcolco.undunion:id/tv_statue")))
        result=self.driver.find_element_by_id("com.vcolco.undunion:id/tv_statue").text
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if assert_it in result:

            write_log('\n' + nowTime + " create car sucessful" + '\n')
            #print '\n' + nowTime + " create car sucessful" + '\n'
            print  colored(('\n' + nowTime + " create car sucessful" + '\n'), "green")

        else:
            write_log(colored(('\n' + nowTime + " create car fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " create car fail" + '\n'), "red")
        self.driver.quit()