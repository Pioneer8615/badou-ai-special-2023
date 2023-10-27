import cv2
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import cv2 as cv
import numpy as np

src = cv.imread("E:/datum/textimage/lena.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

1.##将图像灰度化
'''
Width,Height=src.shape[:2]     #获取图像的宽度和高度
print("src width=",+Width,"src width=", +Height)
##创建一个灰度图像矩阵
gray=np.zeros([Width,Height],src.dtype)
for j in range(Height):
    for i in range(Width):
        value=src[i,j]
        gray[i, j] = int(0.3*value[2]+0.59*value[1]+0.11*value[0])
cv.imshow("Custom method gray image", gray)

##应用opencv对图像灰度化
grayImage=cv.cvtColor(src,cv2.COLOR_BGRA2GRAY)
cv.imshow( "opencv method grayimage",grayImage)
'''

2.#将图像进行二值化

#将图像灰度化

grayImage=cv.cvtColor(src,cv2.COLOR_BGRA2GRAY)
Width,Height=grayImage.shape    #获取图像的宽度和高度
print("src width=",+Width,"src width=", +Height)
##创建一个灰度图像矩阵
'''
for j in range(Height):
    for i in range(Width):
        if (grayImage[i,j]>128):
            grayImage[i, j]=255
        else:
            grayImage[i, j] = 0
'''
'''
grayImage = cv2.normalize(grayImage, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
for j in range(Height):
    for i in range(Width):
        if (grayImage[i,j]>0.5):
            grayImage[i, j]=1
        else:
            grayImage[i, j] = 0

cv.imshow("Custom method threshold image", grayImage)

'''

#应用opencv将图像进行二值化（自适应方式）
'''
thresholeimage=cv.adaptiveThreshold(grayImage,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,9,0)

cv2.imshow('opencv method threshold image',thresholeimage)

'''

#3.图像插值算法
#3.1最近邻插值算法













cv.waitKey(0)
cv.destroyAllWindows()
