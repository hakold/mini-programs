## pip install pillow
## 在头像右上角添加文字
from PIL import Image,ImageDraw,ImageFont

def runchange(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',size=50)
    fillcolor = "red"
    width, height = image.size
    draw.text((width-150,0),'hakold',font=font,fill=fillcolor)
    img.save('result.jpg','jpeg')



if __name__ == '__main__':
    image = Image.open('/resource/0000.jpg')
    runchange(image)
    print('finish')