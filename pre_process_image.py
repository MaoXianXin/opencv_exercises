import cv2
import numpy as np


def preprocess_image(img_path):
    # read the image
    image = cv2.imread(img_path)
    # convert the image to grayscale format
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #---- performed morphological erosion for a rectangular structuring element of kernel size 2
    kernel = np.ones((2, 2), np.uint8)
    erosion = cv2.morphologyEx(img_gray, cv2.MORPH_ERODE, kernel, iterations=2)
    # cv2.imshow("erosion", erosion)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #---- inverted this image and blurred it with a kernel size of 5. The reason for such a huge kernel is to obtain a smooth leaf edge
    ret, thresh1 = cv2.threshold(erosion, 127, 255, 1)
    blur = cv2.blur(thresh1, (5, 5))
    # cv2.imshow("blur", blur)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # ---- again performed another threshold on this image to get the central portion of the edge
    ret, thresh2 = cv2.threshold(blur, 145, 255, 0)
    # cv2.imshow("thresh2", thresh2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # ---- And then performed morphological erosion to thin the edge. used an ellipse structuring element of kernel size 1
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    final = cv2.morphologyEx(thresh2, cv2.MORPH_ERODE, kernel1, iterations=2)
    # cv2.imshow("final", final)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return final
