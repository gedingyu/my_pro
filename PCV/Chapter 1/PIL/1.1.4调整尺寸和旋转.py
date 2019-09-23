from PIL import Image
# resize() 方法。该方法的参数是一个元组，用来指定新图像的大小：
img=Image.open('../empire.png')
new_img=img.resize((150,150))
new_img=new_img.rotate(45)
new_img.show()