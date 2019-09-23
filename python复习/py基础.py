
for i in range(1,10,1):#1-9
    print(i)

for i in range(1, 10, 2):
    print(i)

x,y,z=1,2,10
if x<y<z:
    print('yeah')

#*******************************************
#全局变量
apple=100
b=None
def fun():
    a=10
    global b
    b=22
    print(a)
    return a+100

print(apple)
#print(a)  a是局部变量，不能在后面输出,函数里面可以改动外面，需要加global
print(b)

#************************************************
# 文件读写
# 文件写入
text='This is my first test.\nThis is next line.\nThis is last line'
# print(text)
my_file=open('my file.txt','w')#参数1：文件名。参数2：打开后可进行的功能
my_file.write(text)
my_file.close()
#文件追加
appendtxt='\nthis is my appendtxt'
my_file1=open('my file.txt','a')#a参数表示追加
my_file1.write(appendtxt)
my_file1.close()
# 读文件里的内容
file=open('my file.txt','r')#r参数表示读，file里存了文件
content=file.read()
print(content)

#读每行,#readlines():加s表示一次性全部读
file=open('my file.txt','r')
content_1=file.readline()
content_2=file.readline()
print(content_1,content_2)
file.close()


#***********************************
#input函数
a_input=input('输入一个数：')
print(a_input)

if a_input==1:
    print('int 形式')
else:
    print('str形式')

