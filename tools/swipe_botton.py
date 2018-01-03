#!/usr/bin/env python
# -*- coding: cp936 -*-
from time import sleep
'''
int width = driver.manage().window().getSize().width;
int height = driver.manage().window().getSize().height;
String str1;String str2;
//  do while 循环
do{   
//滑动前获取pagesource
 str1=driver.getPageSource();  
  driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000);    
Thread.sleep(2000);  
//滑动后获取pagesource
  str2=driver.getPageSource(); }while (!str1.equals(str2))'''
from appium import webdriver
def swipeBotton(driver):
    width = driver.manage().window().getSize().width
    height = driver.manage().window().getSize().height
    while 1:
        #滑动前获取pagesource
        str1=driver.getPageSource()
        driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000)
        sleep(1)
        #滑动后获取pagesource
        str2 = driver.getPageSource()



