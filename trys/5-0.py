import cv2


jpg = cv2.imread("1.jpg")
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow(jpg[:, :, 0], jpg)

cv2.waitKey()
cv2.destroyAllWindows()


