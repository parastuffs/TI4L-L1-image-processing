import numpy as np
import cv2
import matplotlib.pyplot as plt

#cam = cv2.VideoCapture(0)
# cam.set(3,640)
# cam.set(4,480)
# while(true):
# 	ret, frame = cam.read()
frame = cv2.imread("akabeko-pink-bg.png")
bg = cv2.imread("bg.png")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
image_mask = cv2.inRange(hsv, np.array([5,80,150]), np.array([6,100,200]))
bg_mask = cv2.bitwise_and(bg,bg,mask=image_mask)
fg_mask = cv2.bitwise_and(frame,frame,mask = cv2.bitwise_not(image_mask))
bg_replaced = cv2.add(bg_mask,fg_mask)
while(True):
	cv2.imshow('Window',bg_replaced)
	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()