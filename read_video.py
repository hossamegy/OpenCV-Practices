import cv2

video_path = r'assets\videoplayback.mp4'

capture = cv2.VideoCapture(video_path)

while True:
    isTrue, frame = capture.read()

    cv2.imshow('video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()