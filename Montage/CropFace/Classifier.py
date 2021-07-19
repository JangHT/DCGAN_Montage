import os
from PIL import Image
import pandas
import pickle
import numpy as np
import sys
import math


print("\n< 옵션 목록 >")

for i in range(len(sys.argv)):
  print("sys.argv[%d] = %s" % (i, sys.argv[i]))

a = list(sys.argv[1])
#new_data = []
cnt = 0

print(a)

data_dir = './datasets/celebA/data'
if not os.path.isdir('./' + sys.argv[1]):
    os.mkdir('./' + sys.argv[1])
save_dir = './' + sys.argv[1]

image_size = 96
crop_size = 150

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

img_list = os.listdir(data_dir)

label = []
selected_label = []


Male_idx = 1
Femail_idx = 2

Narrow_eyes_idx = 3
Wide_eyes_idx = 4

Small_nose_idx = 5
Big_nose_idx = 6

Small_lips_idx = 7
Big_lips_idx = 8

beard_idx = 9
No_beard_idx = 10

High_cheekbones_idx = 11
Low_cheekbones_idx = 12

Young_idx = 13
Old_idx = 14

Eye_glasses_idx = 15
No_eye_glasses_idx = 16

White_idx = 17
Black_idx = 18


selected_label.append(0)
if int(a[0]) == 1:
	selected_label.append(Male_idx)
if int(a[1]) == 1:
	selected_label.append(Femail_idx)
if int(a[2]) == 1:
	selected_label.append(Narrow_eyes_idx)
if int(a[3]) == 1:
	selected_label.append(Wide_eyes_idx)
if int(a[4]) == 1:
	selected_label.append(Small_nose_idx)
if int(a[5]) == 1:
	selected_label.append(Big_nose_idx)
if int(a[6]) == 1:
	selected_label.append(Small_lips_idx)
if int(a[7]) == 1:
	selected_label.append(Big_lips_idx)


if int(a[8]) == 1:
	selected_label.append(beard_idx)
elif int(a[8]) == 0:
	selected_label.append(No_beard_idx)
elif int(a[9]) == 1:
	selected_label.append(High_cheekbones_idx)
elif int(a[9]) == 0:
	selected_label.append(Low_cheekbones_idx)


if int(a[10]) == 1:
	selected_label.append(Young_idx)
if int(a[11]) == 1:
	selected_label.append(Old_idx)
if int(a[12]) == 1:
	selected_label.append(Eye_glasses_idx)
if int(a[13]) == 1:
	selected_label.append(No_eye_glasses_idx)
if int(a[14]) == 1:
	selected_label.append(White_idx)
if int(a[15]) == 1:
	selected_label.append(Black_idx)


print(selected_label)
lenS = len(selected_label)
usecols = tuple(selected_label)
print(usecols)
#new_data.append(len(img_list))

print(lenS)

data = pandas.read_csv('./new_determined_labels.csv', usecols=usecols, dtype='str').values.squeeze()

print(data)

sum = [0]*(len(img_list)+1)
for i in range(1, len(img_list)):
	for j in range(1, lenS):
		y = float(data[i][j])
		x = math.isnan(y)
		if(x != True):
			sum[i] = sum[i] + int(data[i][j])

#print(sum)
	
cc = 0
for i in range(len(sum)):
	if sum[i] == lenS-1:
		sum[i] = sum[i] + 1
		cc = cc + 1
print(cc)
#print(int(data[1][1]))

for i in range(1, len(img_list)):
    if (sum[i] == lenS):
        img = Image.open(open(data_dir + "/" + data[i][0], 'rb'))
        c_x = (img.size[0] - crop_size) // 2
        c_y = (img.size[1] - crop_size) // 2
        img = img.crop([c_x, c_y, c_x + crop_size, c_y + crop_size])
        img = img.resize((image_size, image_size), Image.BILINEAR)
        img.save(save_dir + "/" + data[i][0], 'JPEG')

        for j in range(1, lenS):
            if data[i][j] == -1:
                data[i][j] = 0
			
        #new_data.append(data[i][1])

        cnt += 1
        if cnt % 1000 == 0:
            print('Resizing %s images...' % cnt)
    #else:
        #new_data.append(0)
	
print('Total %d images are resized.' % cnt)

os.system("mv ./" + sys.argv[1] + " ./dataset")

os.system("python3 crop_face.py dataset out 10000 " + sys.argv[1])








#l1 = len(img_list)
#l2 = 0 # set batch_size
#l4 = 0 # set learning_rate

#if l1 < 100:
#    l2 = 10
#    l4 = 0.002
#elif l1 >= 100 and l1 < 1000:
#    l2 = 50
#    l4 = 0.0002
#elif l1 > 1000:
#    l2 = 80
#    l4 = 0.0002

#l3 = str(l2)
#l5 = str(l4)





#with open('./' + sys.argv[1] + '.pkl', 'wb') as fp:
#    pickle.dump(np.array(new_data), fp)

#((int)(data[i][1]) == int(a[0]))
#	and ((int)(data[i][2]) == int(a[1]))
#	and ((int)(data[i][3]) == int(a[2]))
#	and ((int)(data[i][4]) == int(a[3]))
#	and ((int)(data[i][5]) == int(a[4]))
#	and ((int)(data[i][6]) == int(a[5]))
#	and ((int)(data[i][7]) == int(a[6]))
#	and ((int)(data[i][8]) == int(a[7]))
#	and ((int)(data[i][9]) == int(a[8]))
#	and ((int)(data[i][10]) == int(a[9]))
