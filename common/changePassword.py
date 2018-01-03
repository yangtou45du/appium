#!/usr/bin/env python
# -*- coding: cp936 -*-
from time import sleep
from login import login
from tools.myTools import *
import random
from time import sleep
import  time
from pymongo import MongoClient
import pymongo
class changePassword():
    def  __init__(self):
        pass
    def changePassword(self,dict):
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # 连接ora_db数据库，没有则自动创建
        my_set = db.ora_verify  # 使用ora_car集合，没有则自动创建
        my_set.remove({"phone": dict["phone"]})  # 删除验证码
        self.driver = login().LoginByPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()
        # self.driver.find_element_by_id("com.vcolco.undunion:id/iv_back").click() #进去侧边栏
        self.driver.find_element_by_name(u"系统设置").click()#系统设置
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/rl_account_safe')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_account_safe").click()#账号安全
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_updage_pwd").click()#密码设置
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["newPassword"])#新密码
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_re_pwd").send_keys(dict["newPassword"])#重复新密码
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_code").click()#点击验证码
        time.sleep(1)
        myDict = my_set.find({"phone": dict["phone"]})  # 手机号
        myDict1 = {}
        print myDict
        for myDict1 in myDict:
            print myDict1
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        myCode = myDict1['code']
        print myCode
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_code").send_keys(myCode)
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_reset").click()

        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").clear()  # input phone
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["newPassword"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_login").click()  # click login


        return self.driver





