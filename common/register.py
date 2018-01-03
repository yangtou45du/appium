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
import random
class register():
    def __init__(self):
        self.driver=openApp().driver

    def registed(self,dict):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/in_viewpager')))
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.swipe(1000, 500, 100, 500, 2000)  # huadong page
        self.driver.find_element_by_id("com.vcolco.undunion:id/bt_next").click()  # lijitiyan
        try:
            self.driver.hide_keyboard()
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.NAME, U'我要注册')))
        self.driver.find_element_by_name(U'我要注册').click()#我要注册

        self.driver.find_element_by_id("com.vcolco.undunion:id/etPhone").send_keys(dict["phone"])#输入手机号
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_code").click()
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # 连接ora_db数据库，没有则自动创建
        my_set = db.ora_verify  # 使用ora_car集合，没有则自动创建
        myDict = my_set.find({"phone": dict["phone"]})#手机号
        myDict1 = {}
        print myDict
        for myDict1 in myDict:
            print myDict1
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        myCode = myDict1['code']
        print myCode
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_code").send_keys(myCode)#验证码
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["password"])#密码
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btnRegist").click()#注册

        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_pwd')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["password"])  # 密码
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_login").click()  # click login
        '''
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_first_name')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_first_name").clear()
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_first_name").send_keys("li")
        try:
            self.driver.hide_keyboard()
        except:
            pass
        lastName = random.randint(100, 9000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_last_name").clear()
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_last_name").send_keys(lastName)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sex").click()  # 点击性别
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # 点击女
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # 点击确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()  # 点击公营
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # 选择隶属关系
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # 点击确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_service_city").click()  # 点击服务城市
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()  # 选择服务城市
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_nation").click()  # 民族
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # 选择民族
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # 点击确定
        self.driver.swipe(654, 1500, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_idcard").send_keys("511302199901014569")  # 输入身份证号
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_idcard").click()  # 点击修改
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btn_photo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # 手机相册选择
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # 选择相册
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # 点击确定
        self.driver.swipe(654, 1100, 654, 100, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_carcard_time").click()  # 初领日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_end_tiem").click()  # 有效期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_type").click()  # 准驾车型
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # C2
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_carcard").click()  # 点击修改
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # 选择相册
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # 选择相片
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # 确定
        self.driver.swipe(654, 1770, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_workid").send_keys("REWTWRFEW")  # 资格证
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_workid_end_time").click()  # 有效期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_workcard").click()  # 点击修改
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # 选择相册
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # 选择相片
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # 确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_submit").click()  # 点击提交
        '''
        return self.driver




