###使用PIL生成简易验证码###
from PIL import Image,ImageFont,ImageDraw,ImageFilter 
import random

###生成随机字母###
def randchar():
    return chr(random.randint(65,90))
###65-90表示26个大写字母###

###生成随机数字###
def randnum():
    return random.randint(0,10)

###生成背景颜色###
def backcolor():
    return (random.randint(128,255),random.randint(128,255),random.randint(128,255))

###生成字体颜色###
def wordcolor():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 240
height = 60
###尺寸240*60###

image = Image.new("RGB",(width,height),(255,255,255))
font = ImageFont.truetype('C\Windows\Fonts\ARIALN.TTF',36)

###Windows系统自带字体，可更换###
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range (height):
        draw.point((x,y),backcolor())

for i in range(4):
    draw.text((60*i+10,10),randchar(),fill = wordcolor(),font = font)

image = image.filter(ImageFilter.BLUR)
image.save("randcode.jpg","jpeg")
