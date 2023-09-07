import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import unsharp_mask


# This is the unsharp mask code I havent used but pasted here from stack overflow to understand what was happening
# def unsharp_mask(image, kernel_size=(3, 3), sigma=3, amount=2, threshold=2):
#     """Return a sharpened version of the image, using an unsharp mask."""
#     blurred = cv2.GaussianBlur(image, kernel_size, sigma)
#     sharpened = float(amount + 1) * image - float(amount) * blurred
#     sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
#     sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
#     sharpened = sharpened.round().astype(np.uint8)
#     if threshold > 0:
#         low_contrast_mask = np.absolute(image - blurred) < threshold
#         np.copyto(sharpened, image, where=low_contrast_mask)
#     return sharpened


def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower_parameter = int(max(0, (1.0 - sigma) * v))
    upper_parameter = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower_parameter, upper_parameter)
    return edged

img = cv2.imread('srava.png')
auto_canny(img)
cv2.imshow('k',img)
cv2.imwrite('C:/Users/N/Desktop/Test_gray.jpg', image_gray)
