import cv2
import numpy as np
import matplotlib.pyplot as plot


img = plot.imread("lena.jpg")
gammar_change = [np.power(x/255, 2) * 255 for x in range(256)]#查找表
gammar_img = np.round(np.array(gammar_change)).astype(np.uint8)#四舍五入
img_corrected = cv2.LUT(img, gammar_img)
plot.subplot(121)
plot.imshow(img)
plot.subplot(122)
plot.imshow(img_corrected)
plot.show()
