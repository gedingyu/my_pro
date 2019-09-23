try:
    file=open('abc.txt','w')
except Exception as a:#有异常走这路
    print('no this file')
    response=input('do you want to create a new file?')
    if response=='y':
        file=open('abc.txt','w')
    else:
        pass
else:#没有异常走这路
    file.write('sussess')
file.close()