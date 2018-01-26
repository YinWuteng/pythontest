from PIL import Image, ImageFilter

# 打开源文件图片
im = Image.open('ic_robot_location.png')
assert isinstance(im, Image.Image)
# 获取图像尺寸
w, h = im.size
print('Original image size:%sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w / 2, h / 2))
print('Resize image to:%sx%s' % (w / 2, h / 2))
# 把缩放后的图像用png格式保存
im.save('thumbnail.png', 'png')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blue.png', 'png')
