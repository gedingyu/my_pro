# from PCV.tool.imtools import *
from PIL import Image
import os
import pickle
dir_l=os.path.abspath(os.path.dirname(__file__))#abspath获取根目录
print(dir_l)
outfile_list=os.listdir(dir_l+'\FileList')#获取某文件下的所有图片的名字

for infile in outfile_list:
    # print(infile)
    # print(os.path.splitext(infile))
    # print (os.path.splitext(infile)[0])
    print(infile)
    # print(im)
    outfile=os.path.splitext(infile)[0]+".png"#换后缀
    # print outfile
    im=Image.open(dir_l+'\FileList\\'+infile).save(outfile)#存文件

    # Image.open(im).save(outfile)
