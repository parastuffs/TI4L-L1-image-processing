import cv2
import time
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frames = 10 # total number of frames to capture
delay = 0.5 # delay in seconds
for i in range(frames):
	ret, frame = cam.read()
	cv2.imwrite(f"img_{str(i+1).zfill(2)}.jpg", frame)
	time.sleep(delay)
cam.release()