import numpy as np
import cv2

# Read an image
img_path = r"assets\2.jpg"
img = cv2.imread(img_path)

# Translate
def translate(img, x, y):
    transMat = np.float32([[1, 0, x],[0, 1, y]])
    dims = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dims)

translated_img = translate(img, 120, 120)
cv2.imshow('Translate', translated_img)

# Rotate
def rotate(img, angle, rotatePoint=None):
    (width, height) = img.shape[1], img.shape[0]
    if rotatePoint is None:
        rotatePoint = (width//2, height//2)
    rotateMat = cv2.getRotationMatrix2D(rotatePoint, angle, 1.0)
    return cv2.warpAffine(img,  rotateMat, (width, height))

rotated_img = rotate(img, 60)
cv2.imshow('Rotate', rotated_img)

# Flip 
fliped_img = cv2.flip(img, 0)
cv2.imshow('Flip ', fliped_img)

cv2.waitKey(0)
