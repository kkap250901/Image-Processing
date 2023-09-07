from Noise_Reduction import Nmeans_Deionising
from Noise_Reduction import N_Means_Coloured
from Noise_Reduction import Median_blur
from Noise_Reduction import Fourier_Transform
from Noise_Reduction import BilateralFilter
from Noise_Reduction import Low_Pass_filter

import cv2

img = cv2.imread(
    'C:/Users/kushk/Desktop/University/2nd Year/Data '
    'Science/Cw/l2-ip-assignment/l2-ip-assignment/l2-ip-images/test/corrupted/test002.png')

image1 = N_Means_Coloured(img)
image2 = BilateralFilter(img)
image3 = Median_blur(img)
image4 = Fourier_Transform(img) # This here is for the fourier transform of the image talking about the high and low freq and stuff
# image5 = Butterworth_Low_Pass(image4, 394, 400, 2)) # This here to show how to apply the filter what it does and showing how it reduced the nosie
# But also tlak about how it doesnt remove salt and pepper noise like median so both of both of them have to be used if salt and pepper used]
cv2.imshow('N_means', image1)
cv2.imshow('Bilateral', image2)
cv2.imshow('Median', image3)
# cv2.imshow('Fourier Transform', image4)
# cv2.imshow('Low Pass Filter', image5)
cv2.waitKey(0)
cv2.destroyAllWindows

# Image 1 = N_means_coloured
#Image2 = Bilateral
#Image 3 = Median
#Image 4 = Fourier
#Image 5 = Low pass on FOurier
# Image 6 = Low Pass + Median
# Talk about asthetically whiich removes the most noise and looks the best and preserves the most edges from noisse reduction and stuff