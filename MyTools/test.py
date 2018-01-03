from PIL import ImageColor
from PIL import Image
import pyautogui
from pyocr import pyocr
from PIL import Image
'''Get RGBA'''
#A=ImageColor.getcolor("red",'RGBA')
#print A
'''pillow'''
catIm=Image.open("C:\\Users\\Administrator\\PycharmProjects\\aapium\\testDate\\login_fail.png")
#print catIm
#openPhoto.save("C:\\Users\\Administrator\\PycharmProjects\\aapium\\testDate\\login_fail.jpg")
#newPhoto=Image.new('RGBA',(100,200),'RED')
#newphoto.save("new.png")

#croppedIm=catIm.crop((335,345,565,560))
#croppedIm.save('cropped.png')

#catCopyIm=catIm.copy()
#faceIm=catIm.crop((335,345,565,560))
#print faceIm.size
#catCopyIm.paste(faceIm,(0,0))
#catCopyIm.paste(faceIm, (400, 500))
#catCopyIm.save('pasted.png')

import time
def getTime(self):
    tamp=int(time.time())
    return tamp

def getScreenShot(self):
    time=self.getTime()
    filename='../jpg/%s.png'%time
    self.driver.getScreenShot(filename)
from PIL import ImageGrab
pic=ImageGrab.grab()
pic.save('1.png')
tools = pyocr.get_available_tools()[:]
result=tools[0].image_to_string(Image.open('1.png'), lang='chi_sim')
print result
