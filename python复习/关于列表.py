a=[10,20,30,40,50,60]
a.append(0)
a.insert(1,77)#在位置1处添加77
print(a)
a.remove(20)#移除第一个出现20的
print(a)

#索引取值
print(a[0])
print(a[-1])
print(a[0:3])#输出第0位到第2位，第3位之前
print(a[3:])#第3位后面所有
print(a[-3:])#倒数第3位后面所有

print(a.index(40))#打印40的索引

print(a.count(50))#统计50出现的次数

a.sort()#排序，默认从小到大
a.sort(reverse=True)#从大到小

#****************************************
#多维列表

multi_a=[[1,2,3],
         [4,5,6],
         [7,8,9]]#三行三列

#多维索引
print(multi_a[0][1])


#字典
#键值对