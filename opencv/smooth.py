import cv2
import numpy as np

# 1 加载一张图片
image_origin = cv2.imread('./data/123.jpg')

# 根据图片的尺寸，等比例缩放图片
size = image_origin.shape
print(size)

# 缩小倍数
mini_num = 1.8
image_resize = cv2.resize(image_origin, (int(size[1] / mini_num), int(size[0] / mini_num)),
                          interpolation=cv2.INTER_CUBIC)

# 创建一个窗口
cv2.namedWindow('image')

# 1、blur—图像均值平滑滤波
# 函数原型：blur(src, ksize, dst=None, anchor=None, borderType=None)
# src：图像矩阵
# ksize：滤波窗口尺寸，元组里必须是奇数
# image_beauty = cv2.blur(image_resize, (3, 3))

# 2、GaussianBlur—图像高斯平滑滤波
# 函数原型：GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
# src：图像矩阵
# ksize：滤波窗口尺寸，元组里必须是奇数
# sigmaX：标准差
# image_beauty = cv2.GaussianBlur(image_resize, (5, 3), 0)

# 3、medianBlur—图像中值滤波
# 函数原型：medianBlur(src, ksize, dst=None)
# src：图像矩阵
# ksize：滤波窗口尺寸，必须是奇数
# image_beauty = cv2.medianBlur(image_resize, 3)


# 4、bilateralFilter—图像双边滤波
# 函数原型：bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
# src：图像矩阵
# d：邻域直径
# sigmaColor：颜色标准差
# sigmaSpace：空间标准差
# value值越大美颜的程度越大
value = 30
image_beauty = cv2.bilateralFilter(image_resize, value, value * 2, value / 2)


# 生成图片
cv2.imwrite('./data/1234.jpg', image_beauty)

# 将两张图片的元组叠加在一起
merged_img = np.hstack([image_resize, image_beauty])

# 展示窗口
cv2.imshow('image', merged_img)

# 窗口等待
cv2.waitKey(0)

# 销毁窗口e
cv2.destroyAllWindows()
