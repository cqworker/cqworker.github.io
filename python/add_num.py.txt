#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cq
'''
在图片上添加数字
'''
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    #基于图片对象获取画板
    draw = ImageDraw.Draw(img)
    #字体
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    #颜色
    fillcolor = "#ff0000"
    #大小
    width, height = img.size
    #调用画板实现图片修改
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    #重新保存
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    #打开图片作为图片对象
    image = Image.open('image.jpg')
    #调用业务方法
    add_num(image)
