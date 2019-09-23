import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
plt.figure(num='1',figsize=(8,5))
plt.plot(x,y1)

# 移动坐标
loc=plt.gca()
loc.spines['top'].set_color('none')
loc.spines['right'].set_color('none')
loc.xaxis.set_ticks_position('bottom')
loc.spines['bottom'].set_position(('data',0))
loc.yaxis.set_ticks_position('left')
loc.spines['left'].set_position(('data',0))

#画虚线
x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='blue')#画点
plt.plot([1,1],[0,y0],'black',linestyle='--',linewidth=2.5)#颜色和样式可以简写为'k--',[1,1],[0,y0]代表x从1到1，y从0到y0
# 添加点的注释
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))#见莫烦
plt.show()