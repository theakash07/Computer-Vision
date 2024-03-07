# Image Gradient and Edge Detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image in grayscale
img = cv2.imread('img_5.png', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian operator with an odd kernel size (e.g., 3)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)

# Convert the result to uint8
lap = np.uint8(np.absolute(lap))

# Compute Sobel gradients in both x and y directions
Sobix = cv2.Sobel(img, cv2.CV_64F, 1, 0)
Sobiy = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# Convert Sobel results to uint8
Sobix = np.uint8(np.absolute(Sobix))
Sobiy = np.uint8(np.absolute(Sobiy))

# Combine Sobel gradients using bitwise OR
sobelcombined = cv2.bitwise_or(Sobix, Sobiy)

# Prepare titles and images for display
titles = ['Original Image', 'Laplacian', 'Sobel (x-direction)', 'Sobel (y-direction)', 'Combined Sobel']
images = [img, lap, Sobix, Sobiy, sobelcombined]

# Display images in a 2x3 grid
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')  # Use 'gray' colormap for grayscale images
    plt.xticks([])
    plt.yticks([])

plt.show()
