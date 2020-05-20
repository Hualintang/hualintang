#图片编辑添加数字
from PIL import Image, ImageDraw, ImageFont



zm = Image.open("2.png")
draw = ImageDraw.Draw(zm)
ft = ImageFont.truetype("songti.ttc",20)
draw.text((400,50),"小埋",font = ft, fill = 'red')
zm


'''
def add_num():
    im = Image.open('2.png')
    xsize, ysize = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("songti.ttc",20)
    draw.text((400,50), '小埋',(250,128,114), font)
    im.show()
add_num()
'''
