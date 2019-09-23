import matplotlib.pyplot as plt
import numpy
x=numpy.linspace(-3,3,50)
y1=2*x+1
y2=x**2
#定义窗口8pm/l';
2
[8l,02]

plt.figure()
#画y1的线
plt.plot(x,y1)
#画y2的线，并且设置颜色，线的宽度，样式
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--')
#设置x,y轴坐标范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#设置x,y轴坐标名称
plt.xlabel('i am x')
plt.ylabel('i am y')

#显示
# plt.show()

new_ticks=numpy.linspace(-1,2,5)
print(new_ticks)
#设置x轴刻度，范围-1~2，刻度是5
plt.xticks(new_ticks)
#设置y轴刻度，并命名
plt.yticks([-2,-1,0,1,2],['a','b','c','d','f'])

#gca='get current axis'//axes可定位到百分比位置处，具体可查阅，以及outward属性
###########
#移动坐标轴
###########

#获取当前坐标轴信息
ca=plt.gca()
#设置右侧和上侧的边框为空
ca.spines['top'].set_color('none')
ca.spines['right'].set_color('none')
#开始移动,边框变为坐标轴

ca.spines['bottom'].set_position(('data',0))
ca.spines['left'].set_position(('data',0.5))

ca.xaxis.set_ticks_position('top')#设置坐标轴上的刻度的显示位置




plt.show()