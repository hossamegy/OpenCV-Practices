import cv2 
import numpy as np


blank = np.zeros((500, 500), dtype='uint8')
cv2.imshow('Blank', blank)

rectangle_img = cv2.rectangle(blank.copy(), (40, 40), (460, 460), 255.0 ,-1)
cv2.imshow('Rectangle', rectangle_img)

circle_img = cv2.circle(blank.copy(), (250, 250), 230, 255.0, -1)
cv2.imshow('Circle', circle_img)

bitwise_and_img = cv2.bitwise_and(rectangle_img, circle_img)
cv2.imshow('Bitwise_and', bitwise_and_img)

bitwise_or_img = cv2.bitwise_or(rectangle_img, circle_img)
cv2.imshow('Bitwise_or', bitwise_or_img)

bitwise_xor_img = cv2.bitwise_xor(rectangle_img, circle_img)
cv2.imshow('Bitwise_xor', bitwise_xor_img)

bitwise_not_img = cv2.bitwise_not(rectangle_img, circle_img)
cv2.imshow('Bitwise_not', bitwise_not_img)

cv2.waitKey(0)