#coding=utf-8
from PIL import Image
from pylab import *

img=array(Image.open('../../picture/empire.jpg'))
#根据矩阵的值来绘制
imshow(img)
#4个点（100,200）（100,500）
x=[100,100,400,400]
y=[200,500,200,500]

#用红色，星状绘制点
plot(x,y,'r*')
#绘制前两个点的连线
plot((100,100),(200,500))
#添加标题，显示绘制的图像
title('testing empire')
#坐标刻度值不显示
axis('off')


show()#在每个脚本里，你只能调用一次 show() 命令，而且通常是在脚本的结尾调用。注意，在 PyLab 库中，我们约定图像的左上角为坐标原点。
"""
plot(x,y) # 默认为蓝色实线
plot(x,y,'r*') # 红色星状标记
plot(x,y,'go-') # 带有圆圈标记的绿线
plot(x,y,'ks:') # 带有正方形标记的黑色虚线
"""

'''
用PyLab库绘图的基本颜色格式命令
颜色
'b' 蓝色
'g' 绿色
'r' 红色
'c' 青色
'm' 品红
'y' 黄色
'k' 黑色
'w' 白色
6 ｜ 第 1 章
用PyLab库绘图的基本线型格式命令
线型
'-' 实线
'--' 虚线
':' 点线
用PyLab库绘图的基本绘制标记格式命令
标记
'.' 点
'o' 圆圈
's' 正方形
'*' 星形
'+' 加号
'x' 叉号

'''