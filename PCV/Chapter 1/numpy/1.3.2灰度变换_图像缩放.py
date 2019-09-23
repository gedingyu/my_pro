#coding=utf-8
from PIL import Image
import  os
from pylab import *
from numpy import *
from tools import  imtools
img=array(Image.open('../../picture/empire.jpg.').convert('L'))
# print(img)
im2=255-img#array() 变换的相反操作可以使用 PIL 的 fromarray() 函数完成
print(im2)

im3=(100.0/255)*img+100

im4=255.0*(img/255.0)**2

figure()
gray()#灰度处理
subplot(231)#subplot 后的131代表3个参数，第一行3个图像的第一个
imshow(im2)
axis('off')
title(r'$f(x)=255-x$')
#itle为图像标题，Axis为坐标轴, Label为坐标轴标注，Tick为刻度线，Tick Label为刻度注释
subplot(232)
imshow(im3)
axis('off')
title(r'$f(x)=\frac{100}{255}x+100$')

subplot(233)
imshow(im4)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')
show()
#############################################################################
#图像缩放函数
def imresize(im,sz):
    pil_im=Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

