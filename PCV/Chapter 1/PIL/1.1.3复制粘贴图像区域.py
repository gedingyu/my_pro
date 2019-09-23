#coding=utf-8
from PIL import Image
import os
# 四元组的坐标依次是（左，上，右，下）。PIL 中指定坐标系的左上角坐标为（0，0），例如左边距离（0,0）的距离
img=Image.open('../123.png')#上一级的文件目录
box=(50,20,220,230)#
region=img.crop(box).convert('L')


# region=region.transpose(Image.ROTATE_180)#所选区域旋转180度
img.paste(region,box)
img.show()