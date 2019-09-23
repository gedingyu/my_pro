#coding=utf-8
from tools.imtools import compute_average
from numpy import *
from pylab import *
from PIL import  Image
img=array(Image.open('../../picture/empire.jpg'))

averImg=compute_average(img)
print averImg