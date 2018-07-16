## easy guestletter create
## PIL  pip install pillow
## 简单的验证码图片生成
import random
import string
from PIL import Image,ImageDraw,ImageFont

def guestleeter():
    background = Image.open('C:/resource/background.jpg')  #读白色背景图
    draw = ImageDraw.Draw(background)  # 创建一个可用来对image进行操作的对象。对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建。
    font_type = ImageFont.truetype('C:\Windows\Fonts\Courier New\courbi.ttf',size=40) #图片文字的文字类型以及大小设置
    fillcolor = "black" #填充的颜色
    width, height = background.size #获取背景的图片大小
    font_random = string.ascii_letters #导入a-z A-Z的字符
    font_letter = "" #创建空字符串
    for a in range(4): #循环4次获得4个字母
        font_letter += random.choice(font_random)
    draw.text((width-135,0), font_letter, font=font_type, fill=fillcolor) #对image进行文本操作，（位置，文字内容，文字格式，颜色）
    background.save('guestletter.jpg','jpeg') #将处理后的图片保存

if __name__ == '__main__':
    guestleeter()




