import cv2
import numpy as np

def get_center_color(img):
    """
    计算给定图像中间（5，5）像素的均值
    :param img:
    :return:
    """
    w = img.shape[0]
    w = w//2
    h = img.shape[1]
    h = h//2
    data = img[h - 2:h + 2, w - 2:w + 2]
    b,g,r = cv2.split(data)
    return (int(np.mean(b)), int(np.mean(g)), int(np.mean(r)))

if __name__ == '__main__':

    img = cv2.imread(r'../pic/comp_17.jpg',1)
    pixw = [400, 650, 950, 1300, 1650, 1950]
    pixw2 =[550, 800, 1100, 1450, 1800, 2100] 
    #200
    rect_img = img[950:1100, 1950:2100]   #宽*高
    cv2.imshow('cece', rect_img)
    cv2.waitKey()

    b,g,r =get_center_color(rect_img)
    print(r,g,b)

    """
    for i in pixw:
        rect_img = img[240:300, i:i+60]   #宽*高
        cv2.imshow('cece', rect_img)
        cv2.waitKey()

        b,g,r =get_center_color(rect_img)
        print(r,g,b)
    """