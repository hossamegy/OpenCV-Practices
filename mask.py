import cv2
import numpy as np

img_path = r'assets\dog.jpg'

img = cv2.resize(cv2.imread(img_path), (700, 500), interpolation=cv2.INTER_AREA)
cv2.imshow('Image', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')
cv2.imshow('Blank', blank)

rectangle_mask = cv2.rectangle(blank.copy(), (180, 90), (300, 180), 255.0, -1)
cv2.imshow('Rectangle_mask', rectangle_mask)

rectangle_masked_img  = cv2.bitwise_and(img, img, mask=rectangle_mask)
cv2.imshow('Rectangle mask image', rectangle_masked_img)

circle_mask = cv2.circle(blank.copy(), (240, 130), 50, 255.0, -1)
cv2.imshow('Rectangle_mask', circle_mask)

circle_masked_img  = cv2.bitwise_and(img, img, mask=circle_mask)
cv2.imshow('Circle mask image', circle_masked_img)

cv2.waitKey(0)