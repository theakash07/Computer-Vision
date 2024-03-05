import numpy as np
from matplotlib import pyplot as plt
import cv2

# Read the grayscale image from file ('img_3.png')
img = cv2.imread('img_3.png', cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to a binary image
# using thresholding (Morphological Transformation works on binary images)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Create a 5x5 kernel (structuring element) of ones
kernel = np.ones((5, 5), np.uint8)

# Apply morphological operations
erosion = cv2.erode(mask, kernel, iterations=5)  # Erosion
dilation = cv2.dilate(mask, kernel, iterations=2)  # Dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # Opening
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # Closing
mgradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)  # Morphological Gradient
that = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)  # Top-Hat

# Prepare titles and images for display
titles = ['Original', 'Binary Mask', 'Dilation', 'Erosion', 'Opening', 'Closing', 'Gradient', 'Top-Hat']
images = [img, mask, dilation, erosion, opening, closing, mgradient, that]

# Display the images in a grid
for i in range(8):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')  # Show images in grayscale
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
