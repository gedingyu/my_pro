#coding=utf-8
from PIL import Image
from pylab import *
import numpy
img=array(Image.open('../../picture/empire.jpg'))
img1=array(Image.open('../../picture/123.png').convert('L'),'f')
print (img1.shape,img1.dtype)
print img.shape,img.dtype
print img[1]
# 数组切片
'''
im[i,:] = im[j,:] # 将第 j 行的数值赋值给第 i 行
im[:,i] = 100 # 将第 i 列的所有数值设为 100
im[:100,:50].sum() # 计算前 100 行、前 50 列所有数值的和
im[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
im[i].mean() # 第 i 行所有数值的平均值
im[:,-1] # 最后一列
im[-2,:] (or im[-2]) # 倒数第二行
'''