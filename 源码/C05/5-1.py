import cv2
import numpy as np

while True:
    noiseTV = np.random.random((600, 800, 3))
    noiseTV *= 50
    noiseTV = noiseTV.round()
    cv2.imshow(noiseTV, noiseTV)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
