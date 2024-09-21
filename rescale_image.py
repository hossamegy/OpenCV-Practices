import cv2

def rescale(frame, factor= 0.5):
    height = int(frame.shape[0] * factor)
    width = int(frame.shape[1] * factor)

    new_dims = (width, height)

    return cv2.resize(frame, new_dims, interpolation=cv2.INTER_AREA)


img_path = r"assets\hos3.PNG"

img = cv2.imread(img_path)

print(img.shape)

cv2.imshow("hossam", img)
cv2.waitKey(0)

rescaled_img = rescale(img, factor= 0.5)

print(rescaled_img.shape)

cv2.imshow("hossam", rescaled_img)
cv2.waitKey(0)