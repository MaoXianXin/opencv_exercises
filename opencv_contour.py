# 本题主要难点在于点集不连续. 参考 StackOverflow 的 How could I make the discontinuous contour of an image consistant? 可以解决该问题. 这个仓库的方案，可能可以获得更好的结果: https://github.com/ImageMagick/ImageMagick
# 先膨胀再腐蚀, 其实就是闭操作. 闭操作也会平滑轮廓的一部分, 但与开操作相反, 通常会弥合较窄的间断和细长的沟壑, 消除小的孔洞, 填补轮廓线中的断裂
# 1.形态学操作--膨胀
# 2.形态学操作--腐蚀
# 3.取边缘点
# 4.用fillPoly进行填充

import cv2
import numpy as np
from pre_process_image import preprocess_image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--img_path', type=str, default='/home/mao/Documents/test/test1/ian1980_label.png', help='input image path')
opt = parser.parse_args()
origin_img = cv2.imread(opt.img_path)

# read the image
image = preprocess_image(img_path=opt.img_path)
# cv2.imshow("preprocess_image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


points = []
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i, j] == 255:
            points.append([j, i])
points = np.array(points)


cv2.fillPoly(origin_img, pts=[points], color=(0, 0, 255))

# Displaying the image
cv2.imshow("fillPoly", origin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
