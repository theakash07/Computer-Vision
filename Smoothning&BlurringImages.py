import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image ('img_7.png') in color mode (1)
img = cv2.imread('img_7.png', 1)

# Convert the color space of the image from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define a 5x5 kernel for 2D convolution
kernel = np.ones((5, 5), np.float32) / 25

# Apply 2D convolution to the image using the defined kernel
dst = cv2.filter2D(img, -1, kernel)

# Apply simple box blur to the image (5x5 neighborhood)
blur = cv2.blur(img, (5, 5))

# Apply Gaussian blur to the image (5x5 neighborhood, standard deviation = 0)
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply median blur to the image (kernel size = 5x5)
median = cv2.medianBlur(img, 5)

# Apply bilateral filter to the image (parameters: diameter=9, sigmaColor=75, sigmaSpace=75)
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

# Prepare titles and images for display
titles = ['Original Image', '2D Convolution', 'Box Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gblur, median, bilateral_filter]

# Display images in a 3x3 grid
for i in range(6):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')  # Use 'gray' colormap for grayscale images
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()  # Show the plot
