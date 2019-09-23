import matplotlib.pyplot as plt
import numpy as np
x1=np.arange(10)
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),50,alpha=0.75,cmap=plt.cm.hot)#contour代表等高线,8参数代表分成几部分

C=plt.contour(X,Y,f(X,Y),50,colors='black',linewidth=0.5)

plt.clabel(C,inline=True,fontsize=10)

plt.show()


