import cv2

img_path = r"assets\hos3.PNG"

img = cv2.imread(img_path)

print(img)
print(img.shape)

cv2.imshow("hossam", img)
cv2.waitKey(0)