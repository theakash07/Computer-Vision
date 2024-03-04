# Image Thresholding Visualization using Matplotlib
# This script demonstrates thresholding techniques on a grayscale image.
# Instead of creating separate windows for each thresholding method in OpenCV,
# we display them all in a single Matplotlib figure.

import cv2
from matplotlib import pyplot as plt

# Read the input image in grayscale
img = cv2.imread('img_5.png', 0)

# Apply different thresholding methods
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# Define titles for each thresholding method
titles = ['Original Image', 'Binary Image', 'Binary Image Inverse', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

# Display images in a 2x3 grid
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')  # Display grayscale images
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  # Show the entire figure with all thresholded images
