import cv2
import numpy as np

'''
def nearestfunc(img):
    height,width,channels=img.shape
    dstimage=np.zeros((800,800,channels),np.uint8)
    sh=800/height
    sw=800/width
    for i in range(800):
        for j in range(800):
            x=int(i/sh+0.5)
            y=int(j/sw+0.5)
            dstimage[i,j]=img[x,y]
    return dstimage
pass

'''
def mynearestfunc(img):
    height,width,channels=img.shape
    dstimage=np.zeros((800,800,channels),np.uint8)
    sh=800/height
    sw=800/width
    for i in range(800):
        for j in range(800):
            x=int((i+0.5)/sh)
            y=int((j+0.5)/sw)
            dstimage[i,j]=img[x,y]
    return dstimage
pass

img=cv2.imread("E:/datum/textimage/lena.jpg")

##zoom=nearestfunc(img)
zoom=mynearestfunc(img)
print(zoom.shape)
cv2.imshow("src image",img)
cv2.imshow(" Nearest neighbor interpolation",zoom)
cv2.waitKey(0)
