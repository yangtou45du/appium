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
class createCar():#���������û�ע�ᳵ��
    def __init__(self):
        pass

    def createNewCar(self,dict):
        self.driver = login().LoginByPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        myList= connectDb().find({"phone": "13730687504"})#�������ݿ�
        #myList = db.ora_driver
        carId = []
        for myList1 in myList:
            #print myList1
            carId=myList1["generalRole"]["createCars"]
            print carId
        if carId:#����Ѿ�����������ɾ����ǰ����
            connectDb().update({"phone": dict["phone"]}, {'$''set': {"generalRole.createCars": []}})
        WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()#��������
        self.driver.find_element_by_name(u"��������").click()#��������
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnSwitchCar')))
        self.driver.find_element_by_name(u"�ҵĳ���").click()  # �����ҵĳ���
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_add_car").click()#��ʼ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()#������ϵ
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_server_city").click()#�������
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH,"//android.widget.RelativeLayout[@index='0']")))
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='0']").click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH,"//android.widget.RelativeLayout[@index='1']")))
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='0']").click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH,"//android.widget.RelativeLayout[@index='0']")))
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='0']").click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tv_bus_type')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_bus_type").click()#�೵����
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        licensePlateNumber = random.randint(10000, 99999)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_number").send_keys("K"+str(licensePlateNumber))#���ƺ�
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_car_type").click()
        #self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_brand").click()#Ʒ�Ƴ���
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.NAME, U"��̩")))
        self.driver.find_element_by_name(U"��̩").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_color").click()#������ɫ
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.NAME,u"��ɫ")))
        self.driver.find_element_by_name(u"��ɫ").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sub_model").click()#��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_level").click()#�����ȼ�
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        #swipeUp(self.driver,2)
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_seat_num").send_keys(45)#��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_haveseat_num").send_keys(44)#������λ��
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_displacement").send_keys(10)#����������
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_engine_type").click()#����������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_date").click()#��ʻ֤ע������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_annual_verify").click()#��ʻ֤��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_dirvecard_face").click()#����ϴ�

        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_dirvecard_back").click()  # ����ϴ�
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_op_register_date").click()#��Ӫע����Ϣ
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_op_annual_verify_date").click()#��Ӫ��������
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_op_face").click()#�ϴ�������Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_op_back").click()  # �ϴ�������Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_line_num')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_line_num").send_keys("fsd")  # ��·�ƺ�
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_line_end_date").click()  # ��ֹ����
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_line").click()  # �ϴ���·����Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_jqx')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_jqx").send_keys("sdf")  # ������Ϣ
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_jqx").send_keys("10.11")  # ���ս��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_jqx").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_jqx").click()  # �ϴ����յ���Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_szx')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_szx").send_keys(" sdf")  # ������
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_szx").send_keys("10.11")  # ���ս��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_szx").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_szx").click()  # �ϴ����յ���Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_peo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_peo").send_keys(" hgs")  # ��������
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_peo").send_keys("10.11")  # ���ս��
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_peo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_peo").click()  # �ϴ����յ���Ƭ
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_next_step").click()
        #self.driver = createCar().createNewCar(dict)
        '''
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, "com.vcolco.undunion:id/tv_statue")))
        result = self.driver.find_element_by_id("com.vcolco.undunion:id/tv_statue").text
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if u"��ҵ������" in result:
            #write_pass_log('\n' + nowTime + " create car sucessful" + '\n')
            print nowTime + " create car sucessful"

        else:
            #write_fail_log('\n' + nowTime + " create car fail" + '\n')
            print nowTime + " create car fail"
'''
        return self.driver
        #self.driver.find_element_by_id("").click()
        #self.driver.find_element_by_class_name("").click()
#dict={"phone":"13730687504","password":"123456"}
#a=createCar().createNewCar(dict)

