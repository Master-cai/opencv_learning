import cv2
import random
import time


img = cv2.imread("lena.jpg")
print(img.shape)
(width, height, depth) = img.shape
img_width_box = width * 0.2
img_height_box = height * 0.2
for _ in range(90):
    start_pointX = int(random.uniform(0, img_width_box))
    start_pointY = int(random.uniform(0, img_height_box))
    copyImg = img[start_pointX: 200, start_pointY: 200]
    cv2.imshow("test", copyImg)
#    time.sleep(0.1)
    cv2.waitKey(0)
