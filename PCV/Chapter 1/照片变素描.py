#coding=utf-8
import os
from PIL import  Image
from PIL import ImageFilter
dir_root=os.path.abspath(os.path.dirname(__file__))

if __name__=='__main__':
    imagname1=os.listdir(dir_root+'/beatifull')[0]#listdir()返回列表
    imagname2=os.listdir(dir_root+'/beatifull')[1]
    imag1=Image.open(dir_root+'/beatifull//'+imagname1)
    imag2=Image.open(dir_root+'/beatifull//'+imagname2)
    imag1_filtered=imag1.filter(ImageFilter.CONTOUR)#filter中的参数表示检测边缘
    imag2_filtered=imag2.filter(ImageFilter.CONTOUR)
    imag1_filtered.show()
    imag1_filtered.save(dir_root+'/beatifull//'+imagname1,'png')


