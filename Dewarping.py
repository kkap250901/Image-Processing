import cv2
import numpy as np
import scipy.optimize


# height = 394
# width = 1024
# orig_image_coor = np.float32([[20, 20], [944, 6], [15, 386], [964, 374]])
# new_img_coor = np.float32([[0, 0], [width, 0], [0, height], [width, height]])


def dewarping(img):
    height = 394
    width = 1024
    orig_image_coor = np.float32([[31, 29], [953, 17], [25, 384], [973, 384]])
    new_img_coor = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(orig_image_coor, new_img_coor)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result


img = cv2.imread(
    'C:/Users/kushk/Desktop/University/2nd Year/Data '
    'Science/Cw/l2-ip-assignment/l2-ip-assignment/l2-ip-images/test/corrupted/test002.png')
img = dewarping(img)
cv2.imshow('Normal', img)
cv2.waitKey(0)