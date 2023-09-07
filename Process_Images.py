import cv2
from Image_Processing import Processing
import glob
import cv2 as cv
import os

names = []

for file in os.listdir('../l2-ip-images/validation/corrupted'):
    names.append(file)

# sort files by name and consider mac users:

names.sort()
if (".DS_Store" in names):
    names.remove(".DS_Store")

# read images:
path = '../l2-ip-images/validation/corrupted'
for filename in names:
    imageA = cv2.imread(os.path.join(path, filename))
    imageB = Processing(imageA)
    cv2.imwrite('../l2-ip-images/validation/results/' + filename, imageB)

names2 = []

for file in os.listdir('../l2-ip-images/test/corrupted'):
    names2.append(file)

names2.sort()
if (".DS_Store" in names2):
    names2.remove(".DS_Store")

# read images:
path = '../l2-ip-images/test/corrupted'
for filename in names2:
    imageA = cv2.imread(os.path.join(path, filename))
    imageB = Processing(imageA)
    cv2.imwrite('../l2-ip-images/test/results/' + filename, imageB)