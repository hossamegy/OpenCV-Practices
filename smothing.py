import cv2

img_path = r"assets\2.jpg"

img = cv2.imread(img_path)
cv2.imshow('RGB image', img)

# Average
avg_blur_img = cv2.blur(img, (7, 7))
cv2.imshow('Average blur', avg_blur_img)

# Gaussian
gaussian_blur = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian blur', gaussian_blur)

# Median blur
median_blur = cv2.medianBlur(img, 7)
cv2.imshow('Median blur', median_blur)

# Bilateral blur
bilateral_blur = cv2.bilateralFilter(img, 10, 15, 15)
cv2.imshow('Bilateral blur', bilateral_blur)

cv2.waitKey(0)