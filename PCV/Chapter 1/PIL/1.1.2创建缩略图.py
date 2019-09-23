# coding=utf-8
from PIL import Image
from PCV.tools.imtools import get_imlist
import os
pil_im=Image.open('empire.png')
# thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小）
pil_im.thumbnail((128,128))

pil_im.show()