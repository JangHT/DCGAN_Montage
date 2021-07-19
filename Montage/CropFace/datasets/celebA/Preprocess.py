import os
from PIL import Image
import sys

data_dir = './align_5p/'
save_dir = './result/'

image_size = 64
crop_size = 108

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

img_list = os.listdir(data_dir)

for i in range(len(img_list)):
    img = Image.open(data_dir + img_list[i])
 #   c_x = (img.size[0] - crop_size) // 2
 #   c_y = (img.size[1] - crop_size) // 2
 #   img = img.crop([c_x, c_y, c_x + crop_size, c_y + crop_size])
    #img = img.resize((image_size, image_size), Image.BILINEAR)
    img = img.resize((64, 64), Image.BILINEAR)
    img.save(save_dir + img_list[i], 'JPEG')

    if i % 1000 == 0:
        print('Resizing %d images...' % i)