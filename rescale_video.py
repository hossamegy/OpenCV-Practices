import cv2

def rescale(frame, factor= 0.5):
    height = int(frame.shape[0] * factor)
    width = int(frame.shape[1] * factor)

    new_dims = (width, height)

    return cv2.resize(frame, new_dims, interpolation=cv2.INTER_AREA)

video_path = r'assets\videoplayback.mp4'

capture = cv2.VideoCapture(video_path)

while True:
    isTrue, frame = capture.read()

    rescaled_frame = rescale(frame, factor=0.70)

    cv2.imshow('video', rescaled_frame)

    if cv2.waitKey(20) & 0xFF== ord('x'):
        break
capture.release()

cv2.destroyAllWindows()