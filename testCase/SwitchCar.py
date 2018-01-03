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
            if u"ִ����"==taskStatus:
                nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                write_log(colored(('\n' + nowTime + u" ��ǰ��������ʹ���У���ʱ�޷�����" + '\n'), "red"))
                print colored(('\n' + nowTime + u" ��ǰ��������ʹ���У���ʱ�޷�����" + '\n'), "red")

        except:
            WebDriverWait(self.driver, 30, 0.5).until(
                lambda x: x.find_element_by_id("com.vcolco.undunion:id/iv_back")).click()  # ��������
            self.driver.find_element_by_name(u"��������").click()  # ��������
            try:
                if self.driver.find_element_by_id("com.vcolco.undunion:id/tv_net_error"):
                    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    write_log(colored(('\n' + nowTime + u" ��ǰ˾�����޳�����ʹ�ã���ʱ�޷�����" + '\n'), "red"))
                    print colored(('\n' + nowTime + u" ��ǰ˾�����޳�����ʹ�ã���ʱ�޷�����" + '\n'), "red")


            except:
                WebDriverWait(self.driver, 30, 0.5).until(
                    EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnSwitchCar')))
                self.driver.find_element_by_id("com.vcolco.undunion:id/btnSwitchCar").click()  # ѡ��ǰ�ó�

                try:
                    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    result = self.driver.find_element_by_id("com.vcolco.undunion:id/tvTips").text
                    write_log(colored(('\n' + nowTime + u" ��ǰ��������ʹ���У���ʱ�޷�����" + '\n'), "red"))
                    print colored(('\n' + nowTime + u" ��ǰ��������ʹ���У���ʱ�޷�����" + '\n'), "red")

                except:
                    WebDriverWait(self.driver, 30, 0.5).until(
                        EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/tvPlatNum')))
                    carList = self.driver.find_elements_by_id("com.vcolco.undunion:id/tvPlatNum")  # ��ȡ��ǰ���г���
                    #i = 0
                    print len(carList)
                    while 1:
                        i=1
                        for car in carList:

                            car.click()  # ѭ���������
                            licensePlateNumber=car.text#��ȡ��ǰ�������ƺ�
                            #print licensePlateNumber
                            self.driver.find_element_by_id("com.vcolco.undunion:id/btnSwitchCar").click()  # ȷ���л�
                            context = self.driver.find_element_by_id("com.vcolco.undunion:id/tvTips").text  # �жϵ�ǰ�ĳ����Ƿ��ѱ���ʹ��
                            if u"�ó�Ŀǰ������ʹ�ã��Ƿ�ȷ������" in context:
                                self.driver.find_element_by_id("com.vcolco.undunion:id/btnRight").click()  # ���ȷ��
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
                                self.driver.find_element_by_id("com.vcolco.undunion:id/btnLeft").click()#����ٵ�һ��
                                #carList.remove(car)


                        if i == 1:
                            #width = self.driver.manage().window().getSize().width  # ��ȡ��ǰ�ֻ��ֱ���
                            #height = self.driver.manage().window().getSize().height
                            #width =self.driver.get_window_size()['height']# ��ȡ��ǰ�ֻ��ֱ���
                            #height =self.driver.get_window_size()['width']# ��ȡ��ǰ�ֻ��ֱ���
                            str1 = self.driver.page_source()  # ����ǰ��ȡpagesource
                            print str1
                            swipeDown(self.driver,1)
                            str2 = self.driver.page_source()  # �������ȡpagesource
                            print str2
                            nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                            if str1 == str2:
                                write_log(colored(('\n' + nowTime + u" ��ǰ�޳��ɻ�" + '\n'), "red"))
                                print colored(('\n' + nowTime + u" ��ǰ�޳��ɻ�" + '\n'), "red")
                                break

                            else:
                                carList.append(self.driver.find_elements_by_class_name("android.widget.LinearLayout"))

                        else:
                            break
        self.driver.quit()





#dict={"phone":"13730687504","password":"123456"}
#f=SwitchCar()
#f.switch_suc(dict)