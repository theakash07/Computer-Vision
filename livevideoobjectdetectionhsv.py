# Title: Simple Color Detection using OpenCV

# Import necessary libraries
import cv2
import numpy as np

# Function to be used as a placeholder callback for trackbar events
def nothing(x):
    pass

# Create a window named 'Tracking' and setup trackbars for color range selection
cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)  # Lower Hue
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)  # Lower Saturation
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)  # Lower Value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)  # Upper Hue
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)  # Upper Saturation
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)  # Upper Value

# Initialize the camera
cap = cv2.VideoCapture(0)

# Main loop for continuously processing frames
while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    # Optional: Resize the frame to a specific width and height
    # frame = cv2.resize(frame, (512, 400))

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current positions of the trackbars
    l_h = cv2.getTrackbarPos('LH', "Tracking")
    l_s = cv2.getTrackbarPos('LS', "Tracking")
    l_v = cv2.getTrackbarPos('LV', "Tracking")
    u_h = cv2.getTrackbarPos('UH', "Tracking")
    u_s = cv2.getTrackbarPos('US', "Tracking")
    u_v = cv2.getTrackbarPos('UV', "Tracking")

    # Define lower and upper bounds for the HSV color to detect
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Create a mask that identifies the colors in the specified range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the original frame using bitwise AND operation to extract the color
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, the mask, and the result side by side
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # Break the loop if 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# When everything done, release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
