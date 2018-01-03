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
class createCar():#不适用新用户注册车辆
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
        myList= connectDb().find({"phone": "13730687504"})#连接数据库
        #myList = db.ora_driver
        carId = []
        for myList1 in myList:
            #print myList1
            carId=myList1["generalRole"]["createCars"]
            print carId
        if carId:#如果已经创建车辆，删除当前车辆
            connectDb().update({"phone": dict["phone"]}, {'$''set': {"generalRole.createCars": []}})
        WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()#进入侧边栏
        self.driver.find_element_by_name(u"车辆管理").click()#车辆管理
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnSwitchCar')))
        self.driver.find_element_by_name(u"我的车辆").click()  # 进入我的车辆
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_add_car").click()#开始创建车辆
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ship").click()#隶属关系
        self.driver.find_element_by_id("com.vcolco.undunion:id/cbChose").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_server_city").click()#服务城市
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
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_bus_type").click()#班车类型
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        licensePlateNumber = random.randint(10000, 99999)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_number").send_keys("K"+str(licensePlateNumber))#车牌号
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_car_type").click()
        #self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_brand").click()#品牌车型
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.NAME, U"众泰")))
        self.driver.find_element_by_name(U"众泰").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_color").click()#车身颜色
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.NAME,u"黄色")))
        self.driver.find_element_by_name(u"黄色").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_sub_model").click()#车辆类型
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_level").click()#车辆等级
        self.driver.find_element_by_id("com.vcolco.undunion:id/tvName").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        #swipeUp(self.driver,2)
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_seat_num").send_keys(45)#核载人数
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_haveseat_num").send_keys(44)#可售座位数
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_displacement").send_keys(10)#发动机排量
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_engine_type").click()#变速箱类型
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_get_date").click()#行驶证注册日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_annual_verify").click()#行驶证年审日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_dirvecard_face").click()#点击上传

        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_dirvecard_back").click()  # 点击上传
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_op_register_date").click()#运营注册信息
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_op_annual_verify_date").click()#运营年审日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_op_face").click()#上传正面照片
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_op_back").click()  # 上传背面照片
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_line_num')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_line_num").send_keys("fsd")  # 线路牌号
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_line_end_date").click()  # 截止日期
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_line").click()  # 上传线路牌照片
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_jqx')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_jqx").send_keys("sdf")  # 保险信息
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_jqx").send_keys("10.11")  # 保险金额
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_jqx").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_jqx").click()  # 上传保险单照片
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_szx')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_szx").send_keys(" sdf")  # 三责险
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_szx").send_keys("10.11")  # 保险金额
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_szx").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/ly_szx").click()  # 上传保险单照片
        self.driver.find_element_by_id("com.vcolco.undunion:id/btn_photo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/iv_selected").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_right").click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/et_name_peo')))
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_name_peo").send_keys(" hgs")  # 承运人险
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/et_amount_peo").send_keys("10.11")  # 保险金额
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_end_date_peo").click()
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_confirm").click()
        self.driver.swipe(500, 1400, 500, 200, 2000)
        self.driver.find_element_by_id("com.vcolco.undunion:id/tv_ipc_peo").click()  # 上传保险单照片
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
        if u"企业关联中" in result:
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

