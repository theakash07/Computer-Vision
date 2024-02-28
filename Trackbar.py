import cv2
import numpy as np

# Function to print the current trackbar position (used as a callback)
def nothing(x):
    print(x)

# Create a black image (300x512) with 3 channels (BGR)
img = np.zeros((300, 512, 3), np.uint8)

# Create a named window for the image
cv2.namedWindow('image')

# Create three trackbars for B, G, and R channels, initialized to 0, with a max value of 255
# The trackbars will call the 'nothing' function when their values change
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# Main loop
while True:
    # Display the current image with the trackbar values
    cv2.imshow('image', img)

    # Wait for 1 millisecond for a key event
    k = cv2.waitKey(1) & 0xFF

    # If the key is 'Esc' (ASCII code 27), break out of the loop
    if k == 27:
        break

    # Get the current positions of the trackbars
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')

    # Update the image with the new color based on trackbar positions
    img[:] = [b, g, r]

# Close all OpenCV windows
cv2.destroyAllWindows()
