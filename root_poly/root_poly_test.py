import cv2
import numpy as np
import os


def get_A_matrix(x, y):
    """
    :param x: 输入数据,shape:(10, n)
    :param y: 样本的标准数据, shape:(3,n)
    :return: 返回 训练好的系数矩阵A， shape: (3 , 10)
    """
    temp1 = np.dot(x,x.T)
    temp2 = np.dot(x, y.T)
    temp1 = np.linalg.inv(temp1)
    A = np.dot(temp1, temp2)
    return A.T

def get_polynomial(R, G, B):
    """

    :param rgb: 像素点的RGB值,格式(r,g,b)
    :return: 返回构造的多项式，（1，R, G, B, RG, RB, BG, R*R, B*B, G*G）
    """
    R = float(R)
    G = float(G)
    B = float(B)
    #return [1, R, G, B, R*G, R*B, B*G, R*R, B*B, G*G]
    return [R, G, B, (R*G)**0.5, (R*B)**0.5, (B*G)**0.5]
    #return [R, G, B, (R*G)**0.5, (R*B)**0.5, (B*G)**0.5,
            #(R*G*B)**(1/3), (R*G*G)**(1/3), (R*B*B)**(1/3), (G*R*R)**(1/3), (B*R*R)**(1/3), (G*G*B)**(1/3), (B*B*G)**(1/3)]

def create_inputData(image_data):
    """

    :param image_data: 待校正的原始图片
    :return: 返回线性回归需要的输入矩阵, shape:(10, image_data.shape[0] * image_data.shape[1])
    """
    data = []
    for bgr in image_data:
        data.append(get_polynomial(bgr[0], bgr[1], bgr[2]))
    data = np.array(data)
    return data.T


def create_testData(image_data):
    """
    :param image_data: 待校正的原始图片
    :return: 返回线性回归需要的输入矩阵, shape:(10, image_data.shape[0] * image_data.shape[1])
    """
    data = []
    for raw_data in image_data:
        for bgr in raw_data:
            data.append(get_polynomial(bgr[2], bgr[1], bgr[0]))
    data = np.array(data)
    return data.T

def get_stdColor_value(std_color_file):
    """
    构造标准色卡的R,G,B矩阵，shape: (3 , 24)
    :return: 返回标准色卡的R,G,B值，分别用字典和矩阵存储
    """
    color_dict = {}
    std_matrix = []
    color_value_list = np.loadtxt(std_color_file, dtype=np.str, delimiter=',')

    for element in color_value_list:
        color_dict[element[1]] = (int(element[2]), int(element[3]), int(element[4]))
        std_matrix.append([int(element[2]), int(element[3]), int(element[4])])

    std_matrix = np.array(std_matrix)
    return color_dict, std_matrix.T

def recorrect_color(raw_img, A):
    """
    用系数矩阵A对图像进行颜色校正
    :param raw_img: 原始图像
    :param A: 系数矩阵
    :return: 返回校正后的图像
    """
    w = raw_img.shape[0]
    h = raw_img.shape[1]
    
    input_data = create_testData(raw_img)
    corrected_data = np.dot(A, input_data)
    data = []
    for element in corrected_data:
        vec = []
        for value in element:
            if 0.0 <= value <= 255.0:
                vec.append(int(value))
            elif 0.0 > value:
                vec.append(0)
            elif 255.0 < value:
                vec.append(255)
        data.append(vec)

    data = np.array(data)
    data = data.transpose((1, 0))
    new_img = data.reshape((w,h,3))[...,[2,1,0]]
    return new_img


if __name__ == '__main__':
    
    std_color_file = "./std.csv"
    # 载入标准色卡数据
    color_dict, std_matrix = get_stdColor_value(std_color_file)
    camera_color = np.loadtxt("./camera_color3.txt")
    print(camera_color)

    #std_matrix
    # 载入测试色卡图像，生成回归输入数据
    img = cv2.imread(r'../pic/comp_17.jpg',1)
    #imgs, color_img = img_split(img, img_show=True)
    input_data = create_inputData(camera_color)
    
    # 计算回归方程的系数矩阵
    A = get_A_matrix(input_data, std_matrix)

    # 颜色校正
    new_img = recorrect_color(img, A)
    
    cv2.imwrite(r'../pic/17_rootre2_test.png', new_img)
    #cv2.waitKey(0)
   