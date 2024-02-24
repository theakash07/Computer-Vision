import cv2
import numpy as np

"""
More Mouse Event Examples in OpenCV Python
"""

# Mouse callback function
def call_back(event, x, y, flags, params):
    """
    Callback function for mouse events.

    Parameters:
        event (int): The type of mouse event (e.g., cv2.EVENT_LBUTTONDOWN).
        x (int): x-coordinate of the mouse cursor.
        y (int): y-coordinate of the mouse cursor.
        flags (int): Additional information about the event.
        params: Additional parameters (not used in this example).
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Access the pixel values at the clicked point
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        
        # Draw a red circle at the clicked point
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        # Create a new image with the selected color
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]

        # Display the color image
        cv2.imshow("image", mycolorimage)

# Load an image from file
img = cv2.imread('img_1.png', 1)

# Display the initial image
cv2.imshow('image', img)

# Set the mouse callback function for the 'image' window
cv2.setMouseCallback('image', call_back)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey()
cv2.destroyAllWindows()
