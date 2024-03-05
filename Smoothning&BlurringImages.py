import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image from file ('img_6.png') in color mode (1)
img = cv2.imread('img_6.png', 1)

# Convert the color representation from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define a 5x5 kernel for 2D convolution (averaging filter)
kernel = np.ones((5, 5), np.float32) / 25

# Apply 2D convolution to the image using the specified kernel
dst = cv2.filter2D(img, -1, kernel)

# Apply simple box blur to the image
blur = cv2.blur(img, (5, 5))

# Apply Gaussian blur to the image
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# Prepare titles and images for display
titles = ['Original Image', '2D Convolution', 'Box Blur', 'Gaussian Blur']
images = [img, dst, blur, gblur]

# Display the images in a 2x2 grid
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')  # Use 'gray' colormap for grayscale images
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
