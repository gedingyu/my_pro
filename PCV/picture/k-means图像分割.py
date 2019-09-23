#coding=utf-8
#建立工程并导入sklearn包
#加载图片并进行预处理
#加载K-means聚类算法
#对像素点进行聚类并输出
#PIL包：本实验涉及图像的加载和创建，因此需要用到PIL包



import numpy as np
import PIL.Image as image
from pylab import *
from sklearn.cluster import KMeans
import PIL

def loadData(filePath):
    f=open(filePath,'rb') #二进制形式打开文件
    data=[]
    img=image.open(f)
    m,n=img.size
    for i in range(m):
        for j in range(n):
            x,y,z=img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.mat(data),m,n

imgData,row,col=loadData('123.png')

km=KMeans(n_clusters=3)#定义聚类中心的个数为3

#聚类获得每个像素所属的类别
label=km.fit_predict(imgData)
label=label.reshape((row,col))

pic_new=image.new("L",(row,col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j),256/(label[i][j]+1))
pic_new.save("result-bull-4.jpg","JPEG")
print(PIL.version)

