import cv2
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while (True):
	ret, frame = cam.read()
	cv2.imshow('Detected',frame)
	if cv2.waitKey(5) == 27: # Quit with escape key
		break
cv2.destroyAllWindows()
cam.release()