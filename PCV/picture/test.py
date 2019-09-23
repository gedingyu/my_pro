#coding=utf-8
list=[
    [1,2],
    [3,4]
]
get=input()
# print (type(get))
def isex(get):
    for i in list:
        for j in i:
            # print type(j)
            print (j, get)

            if j==get:
                return 1
    return 0

print isex(get)
