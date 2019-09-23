#coding=utf-8
from PIL import Image
from pylab import *

img=array(Image.open('../../picture/empire.jpg').convert('L'))
#figure代表显示图像的框框
figure()
#不适用颜色信息
gray()
#绘制等高线,在原点的左上角显示轮廓图像
contour(img,origin='image')

axis('equal')
axis('off')
show()
figure()
# hist() 函数的第二个参数指定小区间的数目。需要注意的是，因为 hist() 只接受一
# 维数组作为输入，所以我们在绘制图像直方图之前，必须先对图像进行压平处理。
# flatten() 方法将任意数组按照行优先准则转换成一维数组
hist(img.flatten(),256)
show()