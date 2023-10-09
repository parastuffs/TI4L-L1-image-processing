import cv2
import numpy as np
import time
img1 = cv2.imread('parrots.bmp',1)
img2 = cv2.imread('shiba.bmp',1)
for i in np.linspace(0,1,40):
	alpha = i
	beta = 1-alpha
	print(f"ALPHA = {alpha}, BETA = {beta}")
	cv2.imshow('Image Transition',
	cv2.addWeighted(img1,alpha,img2,beta,0))
	time.sleep(0.05)
	if cv2.waitKey(1) == 27 :
		break
cv2.destroyAllWindows()