import os
from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HEIGHT = 640

ext = ['jpg', 'jpeg', 'png']
os.getcwd()
os.chdir(r'D:/python测试/')
path = "D:/python测试/"
files = os.listdir(path)


def process_image(filename, mwidth=640, mheight=1136):
    image = Image.open(filename)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(filename, 'is OK.')
        return
    if 1.0*w/mwidth > 1.0*h/mheight:
        scale = 1.0*w/mwidth
        new_im = image.resize((int(w/scale), int(h/scale)), Image.ANTIALIAS)
    else:
        scale = 1.0*h/mheight
        new_im = image.resize((int(w/scale), int(h/scale)), Image.ANTIALIAS)
    new_im.save('new-'+filename)
    new_im.close()
    
for file in files:
if file.split('.')[-1] in ext:#以.为分隔符保留最后一段
    process_image(file)
