import cv2

img_path = r"assets\2.jpg"

img = cv2.imread(img_path)
cv2.imshow('RGB image', img)

# Converting to gray
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gry_img)

# Make Blur
blur_img = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur image', blur_img)

# Edges
canny = cv2.Canny(gry_img, 17, 17, 17)
cv2.imshow('Canny image', canny)

# Dilate
dilate_img = cv2.dilate(canny, (7, 7), iterations=2)
cv2.imshow('Dilate image', dilate_img)

# Resize
resized_img = cv2.resize(img, (700, 700))
cv2.imshow('Resized image', resized_img)

cv2.waitKey(0)