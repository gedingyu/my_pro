#coding=utf-8
from PIL import Image
from pylab import *

img=array(Image.open('../../picture/empire.jpg'))
imshow(img)
print('please click 3 points')
x=ginput(3)
print ('you clicked:',x)
show()