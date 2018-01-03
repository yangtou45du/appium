#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-


from termcolor import *
from selenium.webdriver.support.wait import WebDriverWait
from tools.write_log import write_log
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from tools.myTools import *
from common.login import login
class SwitchCar():
    def __init__(self):
        pass
    def switch_suc(self,dict):
        #self.driver=switchCar().changeCar(dict)
        self.driver = login().LoginByPassword(dict)
        try:
            closeMarketing(self.driver)
        except Exception as e:
            pass
        try:
            closeCarSetting(self.driver)
        except:
            pass
        try:
            taskStatus=self.driver.find_element_by_id("com.vcolco.undunion:id/tvTaskStatus").text
            if u"执行中"==taskStatus:
                nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                write_log(colored(('\n' + nowTime + u" 当前车辆正在使用中，暂时无法换车" + '\n'), "red"))
                print colored(('\n' + nowTime + u" 当前车辆正在使用中，暂时无法换车" + '\n'), "red")

        except:
            WebDriverWait(self.driver, 30, 0.5).until(
                lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()  # 进入侧边栏
            self.driver.find_element_by_name(u"车辆管理").click()  # 车辆管理
            try:
                if self.driver.find_element_by_id("com.vcolco.undunion:id/tv_net_error"):
                    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    write_log(colored(('\n' + nowTime + u" 当前司机暂无车辆可使用，暂时无法换车" + '\n'), "red"))
                    print colored(('\n' + nowTime + u" 当前司机暂无车辆可使用，暂时无法换车" + '\n'), "red")


            except:
                WebDriverWait(self.driver, 30, 0.5).until(
                    EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnSwitchCar')))
                self.driver.find_element_by_id("com.vcolco.undunion:id/btnSwitchCar").click()  # 选择当前用车

                try:
                    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    result = self.driver.find_element_by_id("com.vcolco.undunion:id/tvTips").text
                    write_log(colored(('\n' + nowTime + u" 当前车辆正在使用中，暂时无法换车" + '\n'), "red"))
                    print colored(('\n' + nowTime + u" 当前车辆正在使用中，暂时无法换车" + '\n'), "red")

                except:
                    WebDriverWait(self.driver, 30, 0.5).until(
                        EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tvPlatNum')))
                    carList = self.driver.find_elements_by_id("com.vcolco.undunion:id/tvPlatNum")  # 获取当前所有车辆
                    #i = 0
                    print len(carList)
                    while 1:
                        i=1
                        for car in carList:

                            car.click()  # 循环点击车辆
                            licensePlateNumber=car.text#获取当前车辆车牌号
                            #print licensePlateNumber
                            self.driver.find_element_by_id("com.vcolco.undunion:id/btnSwitchCar").click()  # 确认切换
                            context = self.driver.find_element_by_id("com.vcolco.undunion:id/tvTips").text  # 判断当前的车辆是否已被人使用
                            if u"该车目前暂无人使用，是否确定换车" in context:
                                self.driver.find_element_by_id("com.vcolco.undunion:id/btnRight").click()  # 点击确定
                                i = 0
                                WebDriverWait(self.driver, 30, 0.5).until(
                                    EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/top_tv_plate')))
                                nowLicensePlateNumber=self.driver.find_element_by_id("com.vcolco.undunion:id/top_tv_plate").text
                                nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                                if licensePlateNumber==nowLicensePlateNumber:
                                    write_log('\n'+nowTime + " SwitchCar sucessful" + '\n')
                                    #print nowTime + " SwitchCar sucessful"
                                    print  colored(('\n' + nowTime + " SwitchCar sucessful" + '\n'), "green")
                                break
                            else:
                                self.driver.find_element_by_id("com.vcolco.undunion:id/btnLeft").click()#点击再等一下
                                #carList.remove(car)


                        if i == 1:
                            #width = self.driver.manage().window().getSize().width  # 获取当前手机分辨率
                            #height = self.driver.manage().window().getSize().height
                            #width =self.driver.get_window_size()['height']# 获取当前手机分辨率
                            #height =self.driver.get_window_size()['width']# 获取当前手机分辨率
                            str1 = self.driver.page_source()  # 滑动前获取pagesource
                            print str1
                            swipeDown(self.driver,1)
                            str2 = self.driver.page_source()  # 滑动后获取pagesource
                            print str2
                            nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                            if str1 == str2:
                                write_log(colored(('\n' + nowTime + u" 当前无车可换" + '\n'), "red"))
                                print colored(('\n' + nowTime + u" 当前无车可换" + '\n'), "red")
                                break

                            else:
                                carList.append(self.driver.find_elements_by_class_name("android.widget.LinearLayout"))

                        else:
                            break
        self.driver.quit()





#dict={"phone":"13730687504","password":"123456"}
#f=SwitchCar()
#f.switch_suc(dict)