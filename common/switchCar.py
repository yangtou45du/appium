#!/usr/bin/env python
# -*- coding: cp936 -*-
from time import sleep
from login import login
from tools.myTools import *
class switchCar():
    def __init__(self):
        pass

    def changeCar(self,dict):
        self.driver = login().LoginByPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass

        WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()#��������
        self.driver.find_element_by_name(u"��������").click()#��������
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnSwitchCar')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/btnSwitchCar").click()#ѡ��ǰ�ó�
        return self.driver






#dict={"phone":"18582053852","password":"123456"}
#f=switchCar().changeCar(dict)
