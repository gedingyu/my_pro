import numpy as np
import matplotlib.pyplot as plt

n=12
X=np.arange(n)#生成0~11的数
# Y1=((1-X)/float(n))*np.random.uniform(0.5,1.0,n)#生成0.5~1的12个Y1
Y1=(np.arange(12))/10
Y2=(np.arange(12))/10
# Y2=((1-X)/float(n))*np.random.uniform(0.5,1.0,n)
print(Y1)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')#主题和边框颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x,y,'%0.2f'%y,ha='center',va='bottom')#

for x, y in zip(X, Y2):
    plt.text(x, -y, '%0.2f' % -y, ha='center', va='top')

plt.xlim(-5,n)
plt.ylim(-1.25,1.25)
plt.show()