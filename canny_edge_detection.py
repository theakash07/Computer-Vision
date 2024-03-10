# Import necessary libraries
import cv2  # For OpenCV functions
import numpy as np  # For numerical operations (though not explicitly used in this snippet)
from matplotlib import pyplot as plt  # For plotting (though not used in this revised snippet)

# Define a function to update the Canny edge detection parameters
def update_canny(x):
    # Access global variables within the function
    global img, canny
    # Get the current positions of the 'Lower' and 'Upper' trackbars to set as thresholds
    lower = cv2.getTrackbarPos('Lower', 'image')
    upper = cv2.getTrackbarPos('Upper', 'image')
    # Apply the Canny edge detection with the current trackbar values as thresholds
    canny = cv2.Canny(img, lower, upper)
    # Display the result of the Canny edge detection in the 'image' window
    cv2.imshow('image', canny)

# Create a named window where the images and trackbars will be displayed
cv2.namedWindow('image')

# Load an image from file in grayscale mode
img = cv2.imread('img_4.png', cv2.IMREAD_GRAYSCALE)
# Check if image loading was successful
if img is None:
    raise FileNotFoundError("The specified image file was not found.")

# Initial lower and upper threshold values for the Canny edge detection
lower = 100
upper = 200
# Apply initial Canny edge detection to the image with the initial thresholds
canny = cv2.Canny(img, lower, upper)

# Create a trackbar named 'Lower' in the 'image' window
# It starts with the value 'lower', goes up to 255, and calls 'update_canny' whenever moved
cv2.createTrackbar('Lower', 'image', lower, 255, update_canny)

# Similar to 'Lower', create an 'Upper' threshold trackbar in the 'image' window
cv2.createTrackbar('Upper', 'image', upper, 255, update_canny)

# Wait for a key press before closing the windows
cv2.waitKey(0)
# Destroy all windows created by OpenCV to free up resources
cv2.destroyAllWindows()
