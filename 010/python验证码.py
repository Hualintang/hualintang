from PIL import Image, ImageDraw, ImageFont, ImageFilter#ImageFilter滤镜模块
import random
import os
os.chdir('D:/python测试/')

# 240 x 60:
width = 60 * 4
height = 60

#创建指定大小白色图片
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象:
font = ImageFont.truetype('D:/python测试/ziti.ttf', 36)#导入字体类型和大小

# 创建Draw对象:
draw = ImageDraw.Draw(image)


# 随机图片颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
        
# 大写随机字母:
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))   
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())


image = image.filter(ImageFilter.BLUR)# 加模糊滤镜
image.save('yanzhengma1.jpg', 'jpeg')
