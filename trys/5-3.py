import cv2
import numpy as np


img = np.mat(np.zeros((300, 300)))
imgByteArray = bytearray(img)
print(imgByteArray)
imgBGR = np.array(imgByteArray).reshape(300, 300)
cv2.imshow("cool", imgBGR)
cv2.waitKey(0)
