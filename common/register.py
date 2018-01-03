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
            EC.presence_of_element_located((By.NAME, U'��Ҫע��')))
        self.driver.find_element_by_name(U'��Ҫע��').click()#��Ҫע��

        self.driver.find_element_by_id("com.vcolco.undunion:id/etPhone").send_keys(dict["phone"])#�����ֻ���
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_code").click()
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # ����ora_db���ݿ⣬û�����Զ�����
        my_set = db.ora_verify  # ʹ��ora_car���ϣ�û�����Զ�����
        myDict = my_set.find({"phone": dict["phone"]})#�ֻ���
        myDict1 = {}
        print myDict
        for myDict1 in myDict:
            print myDict1
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"isUse" : "N"}})
        # my_set.update({"phone": dict["phone"]}, {'$''set': {"flag" == true}})
        myCode = myDict1['code']
        print myCode
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_code").send_keys(myCode)#��֤��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["password"])#����
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/btnRegist").click()#ע��

        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_pwd')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_phone").send_keys(dict["phone"])
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_pwd").send_keys(dict["password"])  # ����
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
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sex").click()  # ����Ա�
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # ���Ů
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # ���ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()  # �����Ӫ
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # ѡ��������ϵ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # ���ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_service_city").click()  # ����������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()  # ѡ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_nation").click()  # ����
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # ѡ������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # ���ȷ��
        self.driver.swipe(654, 1500, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_idcard").send_keys("511302199901014569")  # �������֤��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_idcard").click()  # ����޸�
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btn_photo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # �ֻ����ѡ��
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # ѡ�����
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # ���ȷ��
        self.driver.swipe(654, 1100, 654, 100, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_carcard_time").click()  # ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_end_tiem").click()  # ��Ч��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_type").click()  # ׼�ݳ���
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # C2
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_carcard").click()  # ����޸�
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # ѡ�����
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # ѡ����Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # ȷ��
        self.driver.swipe(654, 1770, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_workid").send_keys("REWTWRFEW")  # �ʸ�֤
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_workid_end_time").click()  # ��Ч��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_workcard").click()  # ����޸�
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # ѡ�����
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # ѡ����Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_submit").click()  # ����ύ
        '''
        return self.driver




