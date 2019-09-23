# #coding=utf-8
from PIL import Image
from pylab import *
from numpy import *
from tools.imtools import  histeq

img=array(Image.open('../../picture/empire.jpg').convert('L'))


img2,cdf=histeq(img)

figure()

img3=hist(img.flatten(),256)
show()
figure()
img4=hist(img2.flatten(),256)

show()
figure()
subplot(121)
imshow(img)
subplot(122)
imshow(img2)
show()
#
# # def histeq(im,nbr_bins=256):
# #
# #     imhist,bins=histogram(im.flatten(),nbr_bins,normed=True)
# #     cdf=imhist.cumsum()
# #     cdf=255*cdf/cdf[-1]
# #     im2=interp(im.flatten(),bins[:-1],cdf)
# #     return im2.reshape(im.shap),cdf
#  im=array(Image.open('../../picture/empire.jpg'))
