# Import required libraries
import cv2
import numpy as np

# Create a black image (all zeros) with dimensions (250, 500, 3)
img1 = np.zeros((250, 500, 3), np.uint8)

# Draw a white rectangle on img1 from (200, 0) to (300, 100)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

# Load an image from file named 'img_2.png' (Make sure the file exists in the same directory)
img2 = cv2.imread('img_2.png', 1)

# Resize img2 to match the dimensions of img1 (500x250)
img2 = cv2.resize(img2, (500, 250))

# Perform bitwise NOT operation on img1 and img2
bitimg1 = cv2.bitwise_not(img1)
bitimg2 = cv2.bitwise_not(img2)

# Display the bitwise NOT images
cv2.imshow('bitwise_not_img1', bitimg1)
cv2.imshow('bitwise_not_img2', bitimg2)

# Perform bitwise XOR operation on img1 and img2
bitXor = cv2.bitwise_xor(img1, img2)

# Display the bitwise XOR result
cv2.imshow('bitwise_xor_result', bitXor)

# Perform bitwise OR operation on img1 and img2
bitOr = cv2.bitwise_or(img1, img2)

# Display the bitwise OR result
cv2.imshow('bitwise_or_result', bitOr)

# Perform bitwise AND operation on img1 and img2
bitAnd = cv2.bitwise_and(img1, img2)

# Display the bitwise AND result
cv2.imshow('bitwise_and_result', bitAnd)

# Display the original images img1 and img2
cv2.imshow('original_img1', img1)
cv2.imshow('original_img2', img2)

# Wait for a key event and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
