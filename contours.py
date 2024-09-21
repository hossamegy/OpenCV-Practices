import cv2
import numpy as np

img_path = r'assets\dog.jpg'
def resize(img, factor):
    (width, heigth) = int(img.shape[1] * factor), int(img.shape[0] * factor)
    return cv2.resize(img, (width, heigth),  interpolation=cv2.INTER_AREA)

img = cv2.imread(img_path)
resized_img = resize(img, 0.2)
cv2.imshow('Image', resized_img)

blur_img = cv2.GaussianBlur(resized_img, (7, 7), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur_img)

canny = cv2.Canny(blur_img, 70, 70, 70)
cv2.imshow('Canny', canny)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
blank = np.zeros((700, 700, 3), dtype='uint8')

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow('Black', blank)

cv2.waitKey(0)
