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
class changePhone():
    def  __init__(self):
        pass
    def changePhone(self,dict):
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # ����ora_db���ݿ⣬û�����Զ�����
        my_set = db.ora_verify  # ʹ��ora_car���ϣ�û�����Զ�����
        my_set.remove({"phone": dict["phone"]})  # ɾ����֤��
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
        # self.driver.find_element_by_id("com.vcolco.undunion:id/iv_back").click() #��ȥ�����
        self.driver.find_element_by_name(u"ϵͳ����").click()#ϵͳ����
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/rl_account_safe')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_account_safe").click()#�˺Ű�ȫ
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_change_phone").click()#�����ֻ�
        WebDriverWait(self.driver, 30, 0.5).until(
            lambda x: x.find_element_by_id("com.vcolco.undunion:id/et_code")).click()
        myDict = my_set.find({"phone": dict["phone"]})  # �ֻ���
        myDict1 = {}
        print myDict
        for myDict1 in myDict:
            print myDict1
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        myCode = myDict1['code']
        print myCode
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_code").send_keys(myCode)#������֤��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_next_step").click()#�����һ��
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_phone')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["newPhone"])#�������ֻ���
        self.driver.find_element_by_name(u"��ȡ��֤��").click()
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_phone')))
        newDict = my_set.find({"phone": dict["newPhone"]})  # �ֻ���
        newDict1 = {}
        print newDict
        for newDict1 in newDict:
            print newDict1
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        newCode = newDict1['code']
        print newCode
        self.driver.find_element_by_name(u"����д��֤��").send_keys(newCode)#��д�µ���֤��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, "com.vcolco.undunion:id/tv_change")))
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_change").click()#�������
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btn_login')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").clear()  # input phone
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["newPhone"])
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





