# Importing necessary libraries
import cv2
import numpy as np

# Reading two images to be added
img = cv2.imread('img_2.png', 1)
img2 = cv2.imread('img_1.png', 1)

# Ensuring that images have the same size (512x512 in this case)
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Adding the two images
dst = cv2.add(img, img2)

# Displaying the result
cv2.imshow('Combined Image', dst)

# Waiting for a key event to close the window
cv2.waitKey(0)

# Destroying all OpenCV windows
cv2.destroyAllWindows()
