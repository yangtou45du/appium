#!/usr/bin/env python
# -*- coding: cp936 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from pymongo import MongoClient
import pymongo

def closeMarketing(driver):

    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/iv_close')))
    driver.find_element_by_id("com.vcolco.undunion:id/iv_close").click()  # close quanmingyingxiao
def closeCarSetting(driver):

    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, 'com.vcolco.undunion:id/btnLeft')))

    driver.find_element_by_id("com.vcolco.undunion:id/btnLeft").click()  # �رչ�������
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

# ��Ļ���ϻ���
def swipeUp(driver,time):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = x * 0.5  # x����
    y1 = y *0.75  # ��ʼy����
    y2 = y * 0.25  # �յ�y����
    driver.swipe(x1, y1, x1, y2, time)
#��Ļ���»���
def swipeDown(driver,time):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = x * 0.5  #x����
    y1 = y * 0.25   #��ʼy����
    y2 = y* 0.75   #�յ�y����
    driver.swipe(x1, y1, x1, y2,time)
#��Ļ���󻬶�
def swipLeft(driver,time):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1=x*0.75
    y1=y*0.5
    x2=x*0.05
    driver.swipe(x1,y1,x2,y1,time)
#��Ļ���һ���
def swipRight(driver,time):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1=x*0.05
    y1=y*0.5
    x2=x*0.75
    driver.swipe(x1,y1,x2,y1,time)
def connectDb():
    client = pymongo.MongoClient('120.24.228.227',3717)
    userA = 'ora_data'
    password = 'aaaaa8888'
    client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')

    db = client.ora_db  #����ora_db���ݿ⣬û�����Զ�����
    my_set=db.ora_driver#ʹ��ora_car���ϣ�û�����Զ�����

    return my_set

