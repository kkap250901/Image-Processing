import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

# from Sharpening import unsharp_mask

# Read the image
from skimage.color import rgb2gray


# Median BLur To reduce the Noise
def Median_blur(image, size=5):
    output_img = cv2.medianBlur(image, size)
    return output_img


# To reduce noise but also preserving edges
def BilateralFilter(image, size=7, sigmacolor=10, sigmaspace=10):
    output_img = cv2.bilateralFilter(image, size, sigmacolor, sigmaspace)
    return output_img


def Nmeans_Deionising(image, h=25):
    output_img = cv2.fastNlMeansDenoising(image, None, h, 7, 21)
    return output_img


def N_Means_Coloured(image, h=10):
    output_img = cv2.fastNlMeansDenoisingColored(image, None, h, 7, 21)
    return output_img


def Fourier_Transform(image):
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(image)
    dft = fshift = np.fft.fftshift(f)
    dft_shift = np.fft.fftshift(f)
    # magnitude_spectrum = 20 * np.log(np.abs(dft_shift))
    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()
    return dft_shift


# Amir github Property In the loss pass filter it is used for noise filtering what it does is that it uses the dft
# shift we get from fourier transform and it places a low pass filter on it THis low pass filter onto the dft shift
# with high frequency at the centre and low frequency outside lets the low freequency pass through hence smoothening
# the image and reducing noise, but not salt and pepper noise for which median filter is used
def Low_Pass_filter(width, height, d, n):
    Low_Pass_Filter = np.zeros((height, width, 3), np.float32)
    Centre_point = (width / 2, height / 2)

    for i in range(0, Low_Pass_Filter.shape[1]):  # image width
        for j in range(0, Low_Pass_Filter.shape[0]):  # image height
            radius = max(1, math.sqrt(math.pow((i - Centre_point[0]), 2.0) + math.pow((j - Centre_point[1]), 2.0)))
            Low_Pass_Filter[j, i] = 1 / (1 + pow((radius / d), (2 * n)))
    return Low_Pass_Filter


# Amir github Property In the High pass filter it is used for sharpening what it does is that it uses the dft
# shift we get from fourier transform and it places a high pass filter on it this high pass filter onto the dft shift
# with high frequency at the centre and low frequency outside lets the high freequency pass through hence sharpenning
# the image, which proved very good whilst object detection

def High_Pass_filter(width, height, d, n):
    High_Pass_Filter = np.zeros((height, width, 3), np.float32)
    Centre = (width / 2, height / 2)

    for i in range(0, High_Pass_Filter.shape[1]):  # image width
        for j in range(0, High_Pass_Filter.shape[0]):  # image height
            radius = max(1, math.sqrt(math.pow((i - Centre[0]), 2.0) + math.pow((j - Centre[1]), 2.0)))
            High_Pass_Filter[j, i] = 1 / (1 + pow((d / radius), (2 * n)))
    return High_Pass_Filter
