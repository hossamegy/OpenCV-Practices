import cv2

# PATH
img_path = r'assets\dog.jpg'

img = cv2.imread(img_path)
cv2.imshow('Image', img)

# Gray
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_img)

# HSV
hsv_img = cv2.cvtColor(img,  cv2.COLOR_BGR2HSV)
cv2.imshow('Hsv', hsv_img)

# L*A*B
Lab_img = cv2.cvtColor(img,  cv2.COLOR_BGR2LAB)
cv2.imshow('L*A*B', Lab_img)

cv2.waitKey(0)