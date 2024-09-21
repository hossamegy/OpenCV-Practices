import cv2
import numpy as np

blank = np.zeros((800, 800, 3), dtype='uint8')

cv2.rectangle(
    blank, 
    (0, 0), 
    (blank.shape[1]//2, blank.shape[0]//2), 
    (0, 0, 255), 
    thickness=2
)

cv2.circle(
    blank, 
    (blank.shape[1]//2, blank.shape[0]//2), 
    50, 
    (0, 255, 0), 
    thickness=2
)

cv2.line(
    blank, 
    (0, 0), 
    (blank.shape[1]//2, blank.shape[0]//2), 
    (255, 255, 255), 
    thickness=2
)

cv2.putText(
    blank, 
    "My name is Hossam", 
    (300, 300), 
    cv2.FONT_HERSHEY_TRIPLEX, 
    1.0, 
    (0, 255, 0), 
    thickness=2
)

cv2.imshow('blank', blank)
cv2.waitKey(0)