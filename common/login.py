#!/usr/bin/env python
# -*- coding: cp936 -*-
from openApp import openApp
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tools.myTools import *
from pymongo import MongoClient
import pymongo
import time
class login():
    def __init__(self):
        self.driver=openApp().driver
    def LoginByPassword(self,dict):
        #swipLeft(self.driver,3000)
        #swipLeft(self.driver, 3000)
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/in_viewpager')))
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.find_element_by_id("com.vcolco.undunion:id/bt_next").click()  # lijitiyan
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").clear()  # input phone
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["password"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_login").click()  # click login
        return self.driver
    def loginByDynamicPassword(self,dict):
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # 连接ora_db数据库，没有则自动创建
        my_set = db.ora_verify  # 使用ora_car集合，没有则自动创建
        my_set.remove({"phone":dict["phone"]})
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/in_viewpager')))
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.find_element_by_id("com.vcolco.undunion:id/bt_next").click()  # lijitiyan
        #self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])#输入电话号码
        try:
            self.driver.hide_keyboard()
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tv_login_code')))

        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_login_code").click()#点击动态密码登陆
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])#输入手机号
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_code").click()#获取验证码
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tv_login_pwd')))
        myDict=my_set.find({"phone":dict["phone"]})
        myDict1={}
        print myDict
        for myDict1 in myDict:
            print myDict1
        #my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        #my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        myCode=myDict1['code']
        print myCode
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_code").send_keys(myCode)
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.NAME, u"登录")))
        self.driver.find_element_by_name(u"登录").click()
        return self.driver




       




#dict={"phone":"18782256120"}
#f=login()
#f.loginByDynamicPassword(dict)