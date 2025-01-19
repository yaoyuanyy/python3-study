# 操作图片
# refer to https://liaoxuefeng.com/books/python/third-party-modules/pillow/index.html
import logging

from PIL import Image, ImageFilter

im = Image.open('python_img_00.png')

# 获取图片的尺寸
ww, h = im.size
print("图片的尺寸:", (ww, h))

# 缩放到50%
im.thumbnail((ww/2, h/2))
print("缩放到50% w:{0} h:{1}".format(ww/2, h/2))

# 缩放后的图片保存新的名字
im.save("python_img_00_1.png", "png")



# 让图片变得模糊
im2 = Image.open("python_img_00_1.png")
filteredImage = im2.filter(ImageFilter.BLUR)
filteredImage.save("python_img_00_1_filtered.png", "png")
try:
    filteredImage.save("python_img_00_1_filtered.jpg", "jpeg")
except OSError as error:
    logging.exception("error:", error)
    filteredImage.convert("RGB").save("python_img_00_1_filtered.jpg", "jpeg")
finally:
    print("finally")



