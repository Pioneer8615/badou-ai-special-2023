'''
python implementation of bilinear interpolation
'''
import cv2
import numpy as np


def mybilinear_interpolation(img, out_dim):
    SrcH, SrcW, channel = img.shape
    DstH, DstW = out_dim[1], out_dim[0]
    print("src_h, src_w = ", SrcH, SrcW)
    print("dst_h, dst_w = ", DstH, DstW)
    if SrcH == DstH and SrcW == DstW:
        return img.copy()
    dst_img = np.zeros((DstH, DstW, 3), dtype=np.uint8)
    scale_x, scale_y = float(SrcW) / DstW, float(SrcH) / DstH
    for i in range(3):
        for dst_y in range(DstH):
            for dst_x in range(DstW):
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1, SrcW - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, SrcH - 1)
                # calculate the interpolation
                temp0 = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[src_y0, src_x1, i]
                temp1 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
                dst_img[dst_y, dst_x, i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img


if __name__ == '__main__':
    img = cv2.imread("E:/datum/textimage/lena.jpg")
    dst = mybilinear_interpolation(img, (800, 800))
    cv2.imshow('bilinear interp', dst)
    cv2.waitKey()
