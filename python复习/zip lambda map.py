#zip
a=[1,2,3]
b=[4,5,6]
bond1=list(zip(a,b))#bond1=[(1, 4), (2, 5), (3, 6)]
print(bond1)
print(zip(a,b))
for i,j in bond1:
    print(i/2,j*2)

bond2=list(zip(a,a,b))#bond2=[(1, 1, 4), (2, 2, 5), (3, 3, 6)]
print(bond2)

#lambda的使用
def fun1(x,y):
    return x+y

fun2=lambda x,y:x+y
print(fun1(1,2),fun2(2,3))

#map的使用
#map是把函数和参数邦定在一起
l=list(map(fun1,[100],[99]))
print(map(fun1,[100],[99]))
print(l)