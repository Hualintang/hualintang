from PIL import Image, ImageDraw, ImageFont

'''
sourceFileName = "sg.png"
avatar         = Image.open(sourceFileName)
drawAvatar     = ImageDraw.Draw(avatar)
xSize, ySize = avatar.size
drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
    fill = (255, 100, 0), width = 3)#两个三等分位置分别画了一条宽度为 3 像素的平行线
drawAvatar.line([0.33, 0.67 * ySize, xSize, 0.67 * ySize],\
    fill = (255, 0, 0), width = 3)
drawAvatar.arc([0, 0, xSize, ySize], 0, 90,\
    fill = (125, 99, 125))#Draw 类也提供了 arc(xy, start, end, options) 方法来绘制弧
textsize=20
myFont= ImageFont.truetype("songti.ttc",textsize)#.ttc宋体,.ttf英文字体
drawAvatar.text([0.9 * xSize, 0.1 * ySize],"文豪野犬", fill = (2, 0, 0), font = myFont)
del drawAvatar
avatar
'''

zm = Image.open("2.png")
draw = ImageDraw.Draw(zm)
textsize = 20
ft = ImageFont.truetype("songti.ttc", textsize)
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
