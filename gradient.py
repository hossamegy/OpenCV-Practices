import cv2
import numpy as np


img = cv2.resize(cv2.imread(r'assets\dog.jpg'), (900, 600), interpolation=cv2.INTER_AREA)
cv2.imshow('Image', img)

gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray_img)

# Laplacian
lap = cv2.Laplacian(gray_img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian image', lap)

# Sobal
sobal_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0)
cv2.imshow('Sobal x image', sobal_x)

sobal_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1)
cv2.imshow('Sobal y image', sobal_y)

sobal_combine = cv2.bitwise_or(sobal_x, sobal_y)
cv2.imshow('Sobal combine image', sobal_combine)

cv2.waitKey(0)