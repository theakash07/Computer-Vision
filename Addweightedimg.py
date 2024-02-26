# Importing necessary libraries
import cv2

# Reading two images to be added
img = cv2.imread('img_2.png', 1)
img2 = cv2.imread('img_1.png', 1)

# Ensuring that images have the same size (512x512 in this case)
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Adding two images with specified weights and a constant value
dst = cv2.addWeighted(img, 0.5, img2, 0.5, 3)

# Displaying the result
print(cv2.imshow('Combined Image', dst))

# Waiting for a key event to close the window
cv2.waitKey(0)

# Destroying all OpenCV windows
cv2.destroyAllWindows()
