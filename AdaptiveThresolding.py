# Adaptive Thresholding Example
# This code demonstrates adaptive thresholding techniques on an input image.

import cv2

# Read the input image in grayscale
img = cv2.imread('img_5.png', 0)

# Resize the image to a fixed size (480x380)
img = cv2.resize(img, (480, 380))

# Apply global binary thresholding with a fixed threshold value of 50
_, th1 = cv2.threshold(img, 50, 225, cv2.THRESH_BINARY)

# Apply adaptive thresholding using the mean of the neighborhood
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply adaptive thresholding using Gaussian-weighted mean
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the original image and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Global Binary Thresholding', th1)
cv2.imshow('Adaptive Thresholding (Mean)', th2)
cv2.imshow('Adaptive Thresholding (Gaussian)', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
