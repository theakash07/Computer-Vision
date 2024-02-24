import cv2
import numpy as np

# Load an image from file
img = cv2.imread('img.png', 1)

# Display basic information about the image
print("Image Shape:", img.shape)  # Shape of the image (height, width, channels)
print("Image Size:", img.size)     # Total number of pixels in the image
print("Image Data Type:", img.dtype)  # Data type of the image (e.g., uint8)

# Split the image into its color channels (blue, green, red)
b, g, r = cv2.split(img)

# Merge the color channels back to the original image
img = cv2.merge((b, g, r))

# Display the original image
cv2.imshow('Image', img)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey()
cv2.destroyAllWindows()
