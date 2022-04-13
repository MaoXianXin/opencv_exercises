# 关于第二道题，目前我只能做到这种程度，尽力了
# 1. 锐化图片
# 2. 用Canny算子进行边缘检测
# 3. 进行形态学膨胀操作
# 4. findContours以及drawContours, 另外我把模糊区域保存到本地了

import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--img_path",
    type=str,
    default="./1.png",
    help="input image path",
)
parser.add_argument(
    "--img_save_path",
    type=str,
    default="./1-counterpart.png",
    help="input image path",
)
opt = parser.parse_args()


# load image
img = cv2.imread(opt.img_path)

# sharpen image
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
img = cv2.filter2D(img, -1, kernel)

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# canny
canned = cv2.Canny(gray, 100, 200)

# dilate to close holes in lines
kernel = np.ones((5, 5), np.uint8)
mask = cv2.dilate(canned, kernel, iterations=1)

# find contours
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours
cv2.drawContours(img, contours, -1, (255, 255, 255), -1)
cv2.imwrite(opt.img_save_path, img)

# show
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("canny", canned)
cv2.waitKey(0)
