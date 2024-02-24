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
        # Draw a red circle at the clicked point
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        
        # Store the clicked point in the 'points' list
        points.append((x, y))
        
        # Connect consecutive points with a blue line if there are at least two points
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)

        # Display the updated image
        cv2.imshow('image', img)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Uncomment the line below to load an image from file instead
# img = cv2.imread('img_1.png', 1)

# Display the initial image
cv2.imshow('image', img)

# Initialize an empty list to store mouse-clicked points
points = []

# Set the mouse callback function for the 'image' window
cv2.setMouseCallback('image', call_back)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey()
cv2.destroyAllWindows()
