import cv2
import numpy as np
import scipy


img = cv2.imread("lena.jpg", 0)
#print(img.shape)
cv2.imshow("before", img)
cv2.waitKey(0)
#img = cv2.resize(img, (128, 128))
#cv2.imshow("after", img)
#cv2.waitKey(0)
patch_tree = img[0:128, 0:128]
cv2.imshow("patch", patch_tree)
cv2.waitKey(0)
