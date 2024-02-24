import cv2
import numpy as np

''' Region of Interest '''

def call_back(event, x, y, flags, params):
    """
    Mouse callback function to handle left button clicks.

    Parameters:
        event (int): The type of mouse event.
        x (int): x-coordinate of the mouse cursor.
        y (int): y-coordinate of the mouse cursor.
        flags (int): Additional information about the event.
        params: Additional parameters (not used in this example).
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left Button Down at: ", x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        # Display coordinates on the image
        cv2.putText(img, strXY, (x, y), font, 1, (12, 1, 100), 2)
        
        # Extract the region of interest (ROI) containing the ball
        ball = img[362:569, 414:625]

        # Check if the dimensions of the region match the dimensions of the ball
        if 68 + ball.shape[0] <= 275 and 130 + ball.shape[1] <= 341:
            # Move the ball to the new location in the image
            img[68:68 + ball.shape[0], 130:130 + ball.shape[1]] = ball
            cv2.imshow('win', img)
            cv2.imshow('image', img)
        else:
            print("Invalid region dimensions")

# Read the image
img = cv2.imread('img_2.png', 1)

# Display the original image
cv2.imshow('win', img)

# Set the mouse callback function for the 'win' window
cv2.setMouseCallback('win', call_back)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
