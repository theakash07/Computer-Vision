import cv2
import numpy as np

""" Handle Mouse Events in OpenCV """
""" We can have various events like right-click, left-click """

# Get all available mouse events in OpenCV
Event = [i for i in dir(cv2) if 'EVENT' in i]
print(Event)
# Printing all the available Events

# Mouse callback function
def call_back(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Left mouse button clicked
        print("Left Button Down at: ", x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        # Display coordinates on the image
        cv2.putText(img, strXY, (x, y), font, 1, (12, 122, 0), 2)
        cv2.imshow("image", img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        # Right mouse button clicked
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font1 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strx = f'RGB: {blue}, {green}, {red}'
        # Display RGB values on the image
        cv2.putText(img, strx, (x, y), font1, 1, (100, 23, 10), 2)
        cv2.imshow('image', img)

# Load an image
img = cv2.imread('img_1.png', 1)
cv2.imshow('image', img)

# Set the mouse callback function for the image window
cv2.setMouseCallback('image', call_back)

# Wait for a key event and close all windows when a key is pressed
cv2.waitKey()
cv2.destroyAllWindows()
