import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


def CLAHE(image, clipLimit=3):  # Talk about the comparison between just normlaise and CLAHe as CLahe is better
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit)
    final_image = clahe.apply(image)
    return final_image


def Gamma(image, gamma=1.1):
    final_image = np.power(image, gamma).clip(0, 255).astype(np.uint8)
    return final_image


def Histogram_equalisation(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    final_image = cv2.equalizeHist(image)
    return final_image
