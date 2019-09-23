import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)#生成数据
y1=2*x+1
y2=x**2\
## figure:坐标
## plot：线
## figsize参数：图像的显示比例
##num：图相框的名字

# plt.figure(num='直线',figsize=(10,5))#一个figue代表一个图
# plt.plot(x,y1)

#
# plt.figure(num='对比',figsize=(5,10))
plt.figure(num='对比')

plt.plot(x,y2)
#宽度代表线的宽度
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

# plt.show()
#**************************************************************
#设置坐标轴
#x,y取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#x,y轴名称
plt.xlabel('i am x')
plt.ylabel('i am y')
#换x轴 数据
new_ticks=np.linspace(-1,2,6)
print(new_ticks)
plt.xticks(new_ticks)
plt.show()