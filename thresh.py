import cv2

img = cv2.resize(cv2.imread(r'assets\dog.jpg'), (900, 600), interpolation=cv2.INTER_AREA)
cv2.imshow('Image', img)

# Simple
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray_img)

threshold, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh image', thresh_img)

threshold, inv_thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse thresh image', inv_thresh_img)

# Adaptive
adaptive_thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 5)
cv2.imshow('Adaptive thresh image', adaptive_thresh)

cv2.waitKey(0)