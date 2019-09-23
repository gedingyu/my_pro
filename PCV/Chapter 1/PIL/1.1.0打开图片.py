#coding=utf-8
from PIL import Image
from matplotlib.font_manager import FontProperties
from pylab import  *
#convert中L代表图像的模式
#Python图像处理库PIL的基本概念介绍
# https://blog.csdn.net/icamera0/article/details/50647465
pil_im=Image.open('123.png').convert('L')
subplot(122)
axis('off')
imshow(pil_im)
show()

