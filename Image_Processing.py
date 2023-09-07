# Importing all the Noise Reduction Functions
from Noise_Reduction import Median_blur
from Noise_Reduction import BilateralFilter
from Noise_Reduction import Nmeans_Deionising
from Noise_Reduction import N_Means_Coloured
from Noise_Reduction import Fourier_Transform
from Noise_Reduction import Low_Pass_filter
from Noise_Reduction import High_Pass_filter

# Importing Sharpening as well
from Sharpening import unsharp_mask
from Sharpening import auto_canny

# Importing all the Contrast and Brightness functions
from Contrast import CLAHE
from Contrast import Gamma
from Contrast import Histogram_equalisation

# Importing the Deawarping Function
from Dewarping import dewarping
import cv2
import numpy as np


def Processing(image):
    dft_shift = Fourier_Transform(image)
    High_Pass_Filter = High_Pass_filter(1024, 394, 350, 3)
    Low_Pass_Filter = Low_Pass_filter(1024, 394, 400, 2)
    dft_filtered_high = dft_shift * High_Pass_Filter
    dft_filtered_low = dft_shift * Low_Pass_Filter

    Inversed_hi_dft = np.fft.ifftshift(dft_filtered_high)
    Inversed_lo_dft = np.fft.ifftshift(dft_filtered_low)

    High_Pass_filtered_Image = np.fft.ifft2(Inversed_hi_dft)
    Low_Pass_filtered_Image = np.fft.ifft2(Inversed_lo_dft)

    High_Pass_filtered_Image = np.real(High_Pass_filtered_Image)
    Low_Pass_filtered_Image = np.real(Low_Pass_filtered_Image)

    High_Pass_filtered_Image = np.uint8(High_Pass_filtered_Image)
    Low_Pass_filtered_Image = np.uint8(Low_Pass_filtered_Image)
    Sharpened = Low_Pass_filtered_Image + High_Pass_filtered_Image
    noise_reduced = Median_blur(Sharpened, size=3)  # Salt and Pepper removed
    Dewarped = dewarping(noise_reduced)
    Processed = Gamma(Dewarped, gamma=0.95)
    return Processed



