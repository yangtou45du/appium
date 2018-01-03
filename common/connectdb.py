#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
try:# Python 3.x
    from urllib.parse import quote_plus
except ImportError:# Python 2.x
    from urllib import quote_plus
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient('120.24.228.227',3717)
userA = 'ora_data'
password = 'aaaaa8888'
client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')

db = client.ora_db  #连接ora_db数据库，没有则自动创建
my_set = db.ora_driver#使用ora_car集合，没有则自动创建

for i in  my_set.find({"phone" : "13730687504","generalRole.createCars":{"$""exists":"false"}}):
    print i
'''
from tools.myTools import *
#connectDb().update({"phone" : "13730687504"},{'$''set':{"generalRole.createCars":{}}})
for i in  connectDb().find({"phone" : "13730687504"}):
    print i





