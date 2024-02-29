# Title: Interactive Color Detection with OpenCV

# Import necessary libraries
import cv2
import numpy as np

# Function to be used as a placeholder callback for trackbar events
def nothing(x):
    pass

# Create a window named 'Tracking' and trackbars for adjusting color range
cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

# Main loop for continuously processing frames
while True:
    # Read the input image (in this case, 'img_3.png')
    frame = cv2.imread('img_3.png', 1)

    # Resize the frame to a specific width and height
    frame = cv2.resize(frame, (512, 400))  # Corrected resize function

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get lower and upper bounds for the color to be detected from trackbars
    l_h = cv2.getTrackbarPos('LH', "Tracking")
    l_s = cv2.getTrackbarPos('LS', "Tracking")
    l_v = cv2.getTrackbarPos('LV', "Tracking")
    u_h = cv2.getTrackbarPos('UH', "Tracking")
    u_s = cv2.getTrackbarPos('US', "Tracking")
    u_v = cv2.getTrackbarPos('UV', "Tracking")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Create a binary mask using the specified color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the original frame using bitwise AND operation
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, the color mask, and the result side by side
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # Wait for a key press and check if it's the 'Esc' key (ASCII code 27)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close all OpenCV windows when the loop is exited
cv2.destroyAllWindows()
