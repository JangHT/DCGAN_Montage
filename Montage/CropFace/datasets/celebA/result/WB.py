from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

import numpy as np
import cv2
import sys
import urllib
import scipy.misc
import copy

import os
from PIL import Image
import pandas
import pickle
import numpy as np
import sys
import csv

data_dir = './'
img_list = os.listdir(data_dir)
img_list.sort()
#print(img_list)

Filename = []
# [16 + 2] labels
Male = []
Female = []
Narrow_Eyes = []
Wide_Eyes = []
Small_Nose = []
Big_Nose = []
Small_Lips = []
Big_Lips = []
Beard = []
No_Beard = []
High_Cheekbones = []
Low_Cheekbones = []
Young = []
Old = []
Eyeglasses = []
No_Eyeglasses = []

White = []
Black = []

with open('../../../new_determined_labels_original.csv', mode='r', encoding='utf-8') as f:
	reader = csv.reader(f)
	for row in reader:
		Filename.append(row[0])
		Male.append(row[1])
		Female.append(row[2])
		Narrow_Eyes.append(row[3])
		Wide_Eyes.append(row[4])
		Small_Nose.append(row[5])
		Big_Nose.append(row[6])
		Small_Lips.append(row[7])
		Big_Lips.append(row[8])
		Beard.append(row[9])
		No_Beard.append(row[10])
		High_Cheekbones.append(row[11])
		Low_Cheekbones.append(row[12])
		Young.append(row[13])
		Old.append(row[14])
		Eyeglasses.append(row[15])
		No_Eyeglasses.append(row[16])
		White.append(row[17])
		Black.append(row[18])
		#print(row)


#with open('./new_determined_labels.csv', 'wb') as csvfile:
#	writer = csv.writer(csvfile, delimiter=' ')

j = 0

f = open('../../../new_determined_labels.csv', 'w')

csvWriter = csv.writer(f)

csvWriter.writerow([Filename[j], Male[j], Female[j], Narrow_Eyes[j], Wide_Eyes[j], Small_Nose[j], Big_Nose[j], Small_Lips[j], Big_Lips[j], Beard[j], No_Beard[j], High_Cheekbones[j], Low_Cheekbones[j], Young[j], Old[j], Eyeglasses[j], No_Eyeglasses[j], White[j], Black[j]])

j = j + 1

csvWriter.writerow([Filename[j], Male[j], Female[j], Narrow_Eyes[j], Wide_Eyes[j], Small_Nose[j], Big_Nose[j], Small_Lips[j], Big_Lips[j], Beard[j], No_Beard[j], High_Cheekbones[j], Low_Cheekbones[j], Young[j], Old[j], Eyeglasses[j], No_Eyeglasses[j], White[j], Black[j]])

j = j + 1

for filename in img_list:
	a = str(filename)
	#print(a)
	if a[-1] == 'y':
		break

	image = cv2.imread(a)

	# 31,11   :  18,35 :     45,35
	point_1 = image[32,11] #forehead
	point_2 = image[18,35] #leftcheek
	point_3 = image[45,35] #rightcheek
#	print(point_1[0])
#	print(point_1 , point_2, point_3)
	sum1 = int(point_1[0]) + int(point_2[0]) + int(point_3[0])
	sum2 = int(point_1[1]) + int(point_2[1]) + int(point_3[1])
	sum3 = int(point_1[2]) + int(point_2[2]) + int(point_3[2])
#	print(sum)
	
	csvWriter = csv.writer(f)
	
	if (sum1 + sum2 + sum3) / 3 >= 381:
		#print("White")
		#if j >= 2:
		csvWriter.writerow([Filename[j], Male[j], Female[j], Narrow_Eyes[j], Wide_Eyes[j], Small_Nose[j], Big_Nose[j], Small_Lips[j], Big_Lips[j], Beard[j], No_Beard[j], High_Cheekbones[j], Low_Cheekbones[j], Young[j], Old[j], Eyeglasses[j], No_Eyeglasses[j], '1', '-1'])
	else:
		#print("Black")
		#if j >= 2:
		csvWriter.writerow([Filename[j], Male[j], Female[j], Narrow_Eyes[j], Wide_Eyes[j], Small_Nose[j], Big_Nose[j], Small_Lips[j], Big_Lips[j], Beard[j], No_Beard[j], High_Cheekbones[j], Low_Cheekbones[j], Young[j], Old[j], Eyeglasses[j], No_Eyeglasses[j], '-1', '1'])
		
	j = j + 1






