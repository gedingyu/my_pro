#coding=utf-8

def isxing(getstr):
    getlist=list(getstr)
    i=0
    for i in range(0,len(getlist)-1):
        if '*'==getlist[i]:
            return 0
        else: return 1
b=isxing('*b')
k=1
while(k<=3):
    getstr = raw_input('输入')
    print(isxing(getstr))
    if isxing(getstr)==int(0):
        print k
        k=k+1
    if getstr=='abc':
        print ('yes')
        break;

if k>3:
    print "no chance"

