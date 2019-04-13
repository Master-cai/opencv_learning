import cv2


rect_start = (0, 0)
rect_end = (0, 0)


def on_mouse(event, x, y, flags, param):
    # 鼠标左键按下，抬起，双击
    if event == cv2.EVENT_LBUTTONDOWN:
        global rect_start
        rect_start = (x, y)
        print(rect_start)
    elif event == cv2.EVENT_LBUTTONUP:
        global rect_end
        rect_end = (x, y)
        print(rect_end)


img = cv2.imread("lena.jpg")
cv2.namedWindow('test')
cv2.setMouseCallback("test", on_mouse)
cv2.rectangle(img, rect_start, rect_end, (0, 255, 0), 2)
cv2.imshow("test", img)
while (1):
    cv2.imshow("test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
