import cv2 #cv2 임포트
import numpy as np
from scipy import ndimage

height = 64
width = 64

filename = '1001000010100110_epoch_100.png' # enter your specific image name

def image_1x1 (img):
	x = 63; y = 60;  
	w = 97; h = 96;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_1x1.png',img_trim)

	return img_trim 
	
def image_1x2 (img): 
	x = 160; y = 60;  
	w = 97; h = 96;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_1x2.png',img_trim)

	return img_trim 
	
def image_1x3 (img): 
	x = 256; y = 60; 
	w = 97; h = 96;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_1x3.png',img_trim)

	return img_trim 
	
def image_1x4 (img): 
	x = 353; y = 60; 
	w = 97; h = 96; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_1x4.png',img_trim)

	return img_trim 
	
def image_2x1 (img): 
	x = 63; y = 156;  
	w = 97; h = 96; 
	img_trim = img[y:y+h, x:x+w]
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_2x1.png',img_trim)

	return img_trim 
	
def image_2x2 (img): 
	x = 160; y = 156; 
	w = 97; h = 96; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_2x2.png',img_trim)

	return img_trim 
	
def image_2x3 (img): 
	x = 257; y = 156;  
	w = 96; h = 96; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_2x3.png',img_trim)

	return img_trim 
	
def image_2x4 (img): 
	x = 353; y = 156;  
	w = 97; h = 96; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_2x4.png',img_trim)

	return img_trim 
	
def image_3x1 (img): 
	x = 63; y = 255;  
	w = 97; h = 94;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_3x1.png',img_trim)

	return img_trim 
	
def image_3x2 (img): 
	x = 160; y = 255;  
	w = 97; h = 94; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_3x2.png',img_trim)

	return img_trim 
	
def image_3x3 (img): 
	x = 257; y = 255;  
	w = 97; h = 94; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_3x3.png',img_trim)

	return img_trim 
	
def image_3x4 (img): 
	x = 354; y = 255;  
	w = 96; h = 94; 
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_3x4.png',img_trim)

	return img_trim 
	
def image_4x1 (img): 
	x = 63; y = 349;  
	w = 97; h = 94;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_4x1.png',img_trim)

	return img_trim 
	
def image_4x2 (img): 
	x = 160; y = 349;  
	w = 97; h = 94;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_4x2.png',img_trim)

	return img_trim 
	
def image_4x3 (img): 
	x = 257; y = 349;  
	w = 96; h = 94;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_4x3.png',img_trim)

	return img_trim 
	
def image_4x4 (img): 
	x = 353; y = 349;  
	w = 96; h = 94;
	img_trim = img[y:y+h, x:x+w] 
	img_trim = cv2.resize(img_trim, (width, height), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(filename + '_4x4.png',img_trim)

	return img_trim 
	
org_image = cv2.imread(filename) 
img_1x1 = image_1x1(org_image) # 1x1
img_1x2 = image_1x2(org_image) # 1x2
img_1x3 = image_1x3(org_image) # 1x3
img_1x4 = image_1x4(org_image) # 1x4

img_2x1 = image_2x1(org_image) # 2x1
img_2x2 = image_2x2(org_image) # 2x2
img_2x3 = image_2x3(org_image) # 2x3
img_2x4 = image_2x4(org_image) # 2x4

img_3x1 = image_3x1(org_image) # 3x1
img_3x2 = image_3x2(org_image) # 3x2
img_3x3 = image_3x3(org_image) # 3x3
img_3x4 = image_3x4(org_image) # 3x4

img_4x1 = image_4x1(org_image) # 4x1
img_4x2 = image_4x2(org_image) # 4x2
img_4x3 = image_4x3(org_image) # 4x3
img_4x4 = image_4x4(org_image) # 4x4





