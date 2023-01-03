#!/usr/bin/env python3
import rclpy
import cv2
cap = cv2.VideoCapture(0)
print(cap.isOpened())

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
# cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Cannot open camera")

while True:
    ret, frame = cap.read()
    # print(ret)
    if not ret:
        break
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
