import cv2
import numpy as np

img_path = r'assets\2.jpg'

img = cv2.imread(img_path)
cv2.imshow('Image', img)

r,g,b = cv2.split(img)

print('image', img.shape)
print('R', r.shape)
print('G', g.shape)
print('B', b.shape)

cv2.imshow('R', r)
cv2.imshow('G', g)
cv2.imshow('B', b)

merged_img = cv2.merge([r,g,b])
cv2.imshow('Merge', merged_img)
print('Merge', merged_img.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue_img = cv2.merge([b, blank, blank])
green_img = cv2.merge([blank, g, blank])
red_img = cv2.merge([blank, blank, r])

cv2.imshow('Red image', red_img)
cv2.imshow('Green image', green_img)
cv2.imshow('Blue image', blue_img)
cv2.waitKey(0)