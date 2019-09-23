import numpy as np
import matplotlib.pyplot as plt
n=1024
m=100
X=np.random.normal(0,1,n)#0~1,1024个点，存到列表中
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)#随机公式生成颜色
print(X,Y)
plt.scatter(X,Y,s=75,c=T,alpha=.5)#size=75,颜色为T,alpha:透明度
plt.xlim(-1.5,1.5)
plt.xticks(())
plt.ylim(-1.5,1.5)
# plt.yticks(())#隐藏ticks
plt.show()