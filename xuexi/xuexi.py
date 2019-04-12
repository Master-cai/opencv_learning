import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

single = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]


def initImg(interceptImg):
    for i in range(131, 185):
        for j in range(942, 975):
            for k in range(3):
                interceptImg[i, j, k] = 255
    for i in range(268, 317):
        for j in range(814, 859):
                interceptImg[i, j] = [245, 243, 243]


def changeone(interceptImg):
    for i in range(6, 11):
        img_PIL = Image.fromarray(cv2.cvtColor(interceptImg, cv2.COLOR_BGR2RGB))
        font = ImageFont.truetype("c:/Windows/fonts/msyh.ttc", 50)
        fillColor = (0, 0, 0)
        position = (943, 130)
        string = str(i)
    #    string = string.decode('utf8')
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, string, font=font, fill=fillColor)
        font = ImageFont.truetype("c:/Windows/fonts/msyh.ttc", 40)
        position = (815, 265)
        string = single[i]
        draw.text(position, string, font=font, fill=fillColor)
        img_PIL.save(r'D:\new\python\opencv_learning\xuexi\dist\{}.png'.format(i), 'png')
        img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    #    cv2.putText(interceptImg, "{}".format(str(i)), (935, 187), cv2.FONT_HERSHEY_PLAIN, 4.5, (0, 0, 0), 3)
    #    cv2.imwrite("{}.png".format(i), interceptImg)
        initImg(interceptImg)


def changeThree(interceptImg):
    last = interceptImg[266:317, 859:1020]
    #cv2.imshow("test", last)
    #cv2.waitKey(0)
    last = interceptImg[266:317, 859:1020]
    cv2.imwrite("last.png", last)
    last = cv2.imread("last.png")
    for i in range(266, 317):
        for j in range(859, 1020):
            interceptImg[i, j] = [245, 243, 243]
        for j in range(859, 1020):
            # for k in range(3):
            interceptImg[i, j + 78] = last[i - 266, j - 859]  # 挪标题

    for i in range(136, 190):
        for j in range(1130, 975-30, -1):#逆序
            for k in range(3):
                interceptImg[i, j + 30, k] = interceptImg[i, j, k]#挪评论
    for i in range(11, 100):
        if(i%10 != 0):
            img_PIL = Image.fromarray(cv2.cvtColor(interceptImg, cv2.COLOR_BGR2RGB))
            font = ImageFont.truetype("c:/Windows/fonts/msyh.ttc", 50)
            fillColor = (0, 0, 0)#颜色
            position = (943, 130)#起始位置
            string = str(i)
        #    string = string.decode('utf8')
            draw = ImageDraw.Draw(img_PIL)
            draw.text(position, string, font=font, fill=fillColor)
            font = ImageFont.truetype("c:/Windows/fonts/msyh.ttc", 40)
            position = (815, 265)
            ten = i // 10
            one = i % 10
            string = single[ten] + single [10] + single[one]
            draw.text(position, string, font=font, fill=fillColor)
            img_PIL.save(r'D:\new\python\opencv_learning\xuexi\dist\{}.png'.format(i), 'png')
            img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        #    cv2.putText(interceptImg, "{}".format(str(i)), (935, 187), cv2.FONT_HERSHEY_PLAIN, 4.5, (0, 0, 0), 3)
        #    cv2.imwrite("{}.png".format(i), interceptImg)
            initImg(interceptImg)


if __name__ == "__main__":
    origin = cv2.imread("origin.png")
    (height, width, channel) = origin.shape
    interceptImg = origin[height // 2:height // 2 + 500, 0:width]
    initImg(interceptImg)
    changeone(interceptImg)
    changeThree(interceptImg)


