#!/usr/bin/env python
# -*- coding: cp936 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from login import login
import random
from selenium.webdriver.support.ui import WebDriverWait
from tools.myTools import *

class reIdentified():
    def __init__(self):
        pass
    def reIdentifing(self,dict):
        self.driver = login().LoginByPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()
        #self.driver.find_element_by_id("com.vcolco.undunion:id/iv_back").click() #进去侧边栏
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()#个人认证
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()#重新认证
        self.driver.find_element_by_id("com.vcolco.undunion:id/btnRight").click()#确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_first_name").clear()
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_first_name").send_keys("li")
        try:
            self.driver.hide_keyboard()
        except:
            pass
        lastName=random.randint(100,9000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_last_name").clear()
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_last_name").send_keys(lastName)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sex").click()#点击性别
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#点击女
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()#点击确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()  # 点击公营
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#选择隶属关系
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()#点击确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_service_city").click()  # 点击服务城市
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()#选择服务城市
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_nation").click()  # 民族
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # 选择民族
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # 点击确定
        self.driver.swipe(654, 1500, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_idcard").send_keys("511302199901014569")#输入身份证号
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_idcard").click()#点击修改
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID,'com.vcolco.undunion:id/btn_photo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()#手机相册选择
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()#选择相册
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()#点击确定
        self.driver.swipe(654, 1100, 654, 100, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_carcard_time").click() # 初领日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_end_tiem").click()  # 有效期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_type").click()  # 准驾车型
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#C2
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_carcard").click()#点击修改
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # 选择相册
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  #选择相片
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  #确定
        self.driver.swipe(654, 1770, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_workid").send_keys("REWTWRFEW")#资格证
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_workid_end_time").click()#有效期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_workcard").click()#点击修改
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # 选择相册
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # 选择相片
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # 确定
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_submit").click()#点击提交
        #WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of(self.driver.find_element(by=By.ID,value='com.vcolco.undunion:id/tv_result')))
        return self.driver




#dict={"phone":"13730687504","password":"123456"}
#f=reIdentified()
#f.reIdentifing(dict)
