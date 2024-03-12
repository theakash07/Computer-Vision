# Import the OpenCV library for computer vision tasks.
import cv2
# Import the NumPy library for numerical operations, although it's not directly used in the snippet.
import numpy as np

# Read the grayscale image from the file 'img_6.png'.
img = cv2.imread('img_6.png')

# Create a copy of the original image to preserve the original data.
layer = img.copy()

# Initialize a list to store the Gaussian pyramid layers, starting with the original image layer.
gp = [layer]

# Loop to generate 6 levels of Gaussian pyramid by iteratively applying pyrDown,
# which reduces the image size by blurring followed by downsampling.
for i in range(6):
    layer = cv2.pyrDown(layer)  # Apply Gaussian blurring and downsampling.
    gp.append(layer)            # Add the result to the Gaussian pyramid list.

# After building the Gaussian pyramid, select the top level (smallest image).
layer = gp[5]

# Display the upper level of the Gaussian pyramid.
cv2.imshow('Upper-level Gaussian pyramid', layer)

# Initialize the Laplacian pyramid with the top level of the Gaussian pyramid.
lp = [layer]

# Construct the Laplacian pyramid by iterating from the top of the Gaussian pyramid down.
for i in range(5, 0, -1):  # Iterating backwards through the Gaussian pyramid.
    # Upsample the current Gaussian level to match the next higher level in size.
    guassian_extended = cv2.pyrUp(gp[i])
    # Compute the Laplacian level by subtracting the upsampled image from the next higher Gaussian level.
    laplacian = cv2.subtract(gp[i - 1], guassian_extended)
    # Add the Laplacian level to the pyramid.
    lp.append(laplacian)
    # Display the Laplacian level with a window named as the current iteration index.
    cv2.imshow(str(i), laplacian)

# Display the original image for comparison.
cv2.imshow("Original image", img)

# Wait indefinitely for a key press to proceed.
cv2.waitKey(0)
# Close all OpenCV windows and release resources.
cv2.destroyAllWindows()
