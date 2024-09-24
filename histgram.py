import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_hist(hist, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('num of pixel')
    plt.plot(hist)
    plt.xlim([0, 256])


img = cv2.resize(cv2.imread(r'assets\dog.jpg'), (800, 600), interpolation=cv2.INTER_AREA) 
cv2.imshow('Image', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_img)

gray_hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])


blank = np.zeros(img.shape[:2], dtype='uint8')
rectangle = cv2.rectangle(blank, (230, 100), (330, 220), 255.0, -1)
cv2.imshow('Rectangle', rectangle)

masked_img = cv2.bitwise_and(img, img, mask=rectangle)
cv2.imshow('Masked image', masked_img)

plot_hist(hist=gray_hist, title='Grayscale hist')
plot_hist(hist=gray_hist, title='Masked Grayscale hist')

colorBGR = ('b', 'g', 'r')
for i, color in enumerate(colorBGR):
    colorhist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.title('Color hist')
    plt.xlabel('Bins')
    plt.ylabel('num of pixel')
    plt.plot(colorhist, color=color)
    plt.xlim([0, 256])
    
plt.show()

cv2.waitKey(0)