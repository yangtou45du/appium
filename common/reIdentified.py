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
        #self.driver.find_element_by_id("com.vcolco.undunion:id/iv_back").click() #��ȥ�����
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()#������֤
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()#������֤
        self.driver.find_element_by_id("com.vcolco.undunion:id/btnRight").click()#ȷ��
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
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sex").click()#����Ա�
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#���Ů
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()#���ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()  # �����Ӫ
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#ѡ��������ϵ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()#���ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_service_city").click()  # ����������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_name").click()#ѡ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/rl_nation").click()  # ����
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()  # ѡ������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()  # ���ȷ��
        self.driver.swipe(654, 1500, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_idcard").send_keys("511302199901014569")#�������֤��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_idcard").click()#����޸�
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID,'com.vcolco.undunion:id/btn_photo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()#�ֻ����ѡ��
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()#ѡ�����
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()#���ȷ��
        self.driver.swipe(654, 1100, 654, 100, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_carcard_time").click() # ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_end_tiem").click()  # ��Ч��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_carcard_type").click()  # ׼�ݳ���
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()#C2
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_carcard").click()#����޸�
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # ѡ�����
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  #ѡ����Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  #ȷ��
        self.driver.swipe(654, 1770, 654, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_workid").send_keys("REWTWRFEW")#�ʸ�֤
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_workid_end_time").click()#��Ч��
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_pic_workcard").click()#����޸�
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()  # ѡ�����
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_selected')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()  # ѡ����Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()  # ȷ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_submit").click()#����ύ
        #WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of(self.driver.find_element(by=By.ID,value='com.vcolco.undunion:id/tv_result')))
        return self.driver




#dict={"phone":"13730687504","password":"123456"}
#f=reIdentified()
#f.reIdentifing(dict)
