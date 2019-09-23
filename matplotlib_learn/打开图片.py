from PIL import Image
from pylab import *


pill_im=Image.open('123.png').convert('L')
print(pill_im)
pill_im.show()


