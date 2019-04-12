import numpy as np
import cv2
from scipy import ndimage


kernel33 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

img = cv2.imread("tong.png", 0)
linghtImg = ndimage.convolve(img, kernel33)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow("img", linghtImg)
cv2.waitKey(0)
