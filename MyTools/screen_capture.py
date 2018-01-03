#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ctypes
from ctypes.wintypes import *
import win32clipboard,time,datetime,logging
from win32con import *
import sys,win32api,win32con,uiautomation
from PIL import Image
from numpy import *

class BITMAPFILEHEADER(ctypes.Structure):
    _pack_ = 1  # structure field byte alignment
    _fields_ = [
        ('bfType', WORD),  # file type ("BM")
        ('bfSize', DWORD),  # file size in bytes
        ('bfReserved1', WORD),  # must be zero
        ('bfReserved2', WORD),  # must be zero
        ('bfOffBits', DWORD),  # byte offset to the pixel array
    ]

class BITMAPINFOHEADER(ctypes.Structure):
    _pack_ = 1  # structure field byte alignment
    _fields_ = [
        ('biSize', DWORD),
        ('biWidth', LONG),
        ('biHeight', LONG),
        ('biPLanes', WORD),
        ('biBitCount', WORD),
        ('biCompression', DWORD),
        ('biSizeImage', DWORD),
        ('biXPelsPerMeter', LONG),
        ('biYPelsPerMeter', LONG),
        ('biClrUsed', DWORD),
        ('biClrImportant', DWORD)
    ]

class screen_capture(BITMAPFILEHEADER,BITMAPINFOHEADER):
    def control_screen_capture(self,conf,control=None,lOffset=None, rOffset=None,path=None,update=True):
        win32api.keybd_event(win32con.VK_SNAPSHOT, 0)
        time.sleep(3)
        SIZEOF_BITMAPFILEHEADER = ctypes.sizeof(BITMAPFILEHEADER)
        SIZEOF_BITMAPINFOHEADER = ctypes.sizeof(BITMAPINFOHEADER)
        try:win32clipboard.OpenClipboard()
        except:self.control_screen_capture(conf,control,lOffset, rOffset,path)
        try:
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
                data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            else:
                logging.error('clipboard does not contain an image in DIB format')
                sys.exit(1)
        finally:
            win32clipboard.CloseClipboard()

        bmih = BITMAPINFOHEADER()
        ctypes.memmove(ctypes.pointer(bmih), data, SIZEOF_BITMAPINFOHEADER)

        if bmih.biCompression != BI_BITFIELDS:  # RGBA?
            logging.error('insupported compression type {}'.format(bmih.biCompression))
            sys.exit(1)

        bmfh = BITMAPFILEHEADER()
        ctypes.memset(ctypes.pointer(bmfh), 0, SIZEOF_BITMAPFILEHEADER)  # zero structure
        bmfh.bfType = ord('B') | (ord('M') << 8)
        bmfh.bfSize = SIZEOF_BITMAPFILEHEADER + len(data)  # file size
        SIZEOF_COLORTABLE = 0
        bmfh.bfOffBits = SIZEOF_BITMAPFILEHEADER + SIZEOF_BITMAPINFOHEADER + SIZEOF_COLORTABLE
        if not path:
            path = '.\\image\\%s_%s.bmp' %(datetime.datetime.now().strftime('%Y-%m-%d'),conf['name'])
        bmp_filename = path
        with open(bmp_filename, 'wb') as f:
            f.write(bmfh)
            f.write(data)
        # logging.info('截图保存至 %s 中'%(bmp_filename))
        if control:
            im = Image.open(bmp_filename)
            region = im.crop(control.BoundingRectangle)
            region.save(bmp_filename)
        if lOffset and rOffset:
            l,t,r,b = control.BoundingRectangle
            rect = (int((r - l) * lOffset[0]), int((b - t) * lOffset[1]),int((r - l) * rOffset[0]), int((b - t) * rOffset[1]))
            im = Image.open(bmp_filename)
            region = im.crop(rect)
            region.save(bmp_filename)
        if update:
            im = Image.open(bmp_filename)
            width, height = im.size
            im = im.resize((width * 2, height * 2), Image.ANTIALIAS)
            im = im.convert('RGB')
            # 清理颜色
            a = array(im)
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j][0] > 100:
                        a[i][j] = [255, 255, 255]
                    else:
                        a[i][j] = [0, 0, 0]
            im = Image.fromarray(a)
            #放大图片
            im = im.resize((width*20, height*20), Image.ANTIALIAS)
            im.save(bmp_filename)


if __name__ == '__main__':
    qqmgrVirusPane = uiautomation.PaneControl(searchDepth=2, ClassName='TXGuiFoundation', Name='电脑管家 - 病毒查杀')
    conf = {}
    conf['name'] = 'QQ电脑管家'
    sc = screen_capture()
    sc.control_screen_capture(conf,qqmgrVirusPane)