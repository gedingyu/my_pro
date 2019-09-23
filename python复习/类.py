#coding=utf-8
class Calculator:       #首字母要大写，冒号不能缺
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

#非固有属性，可自由输入的属性
    #name1为自由的属性
    def __init__(self,name,price,hight=1,width=2,weight=3):
        self.name1 = name
        self.price1 = price
        self.h = hight
        self.wi = width
        self.we = weight
# calcu=Calculator()
# calcu.name
# print(calcu.name,calcu.price)
# calcu.add(10,20)
c=Calculator('geding1','geding2')
print(c.name1)
print(c.wi)
import sys
# sys.path.append('G:/Anaconda3/envs/gedingyu/lib/site-packages/PCV')
print sys.path

