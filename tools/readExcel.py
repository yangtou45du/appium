#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd,sys
class Excel():
    def read_it(self, path, index=0):
        data=xlrd.open_workbook(path)
        sheet=data.sheets()[index]
        return sheet
ex=Excel()
table=ex.read_it("C:\\Users\\Administrator\\PycharmProjects\\aapium\\tools\\testData.xlsx")
for rownum in range(0,table.nrows):
    i = table.row_values(rownum)
    print i
