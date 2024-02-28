import cv2
import numpy as np

# Callback function for the trackbars
def nothing(x):
    print(x)

# Create a window named 'image' for displaying the image
cv2.namedWindow('image')

# Create a trackbar 'CP' for controlling a parameter (in the range [100, 400]) with initial value 100
cv2.createTrackbar('CP', 'image', 100, 400, nothing)

# Create a switch trackbar to toggle between On (1) and Off (0) with an initial value of 0
switch = 'On : 1\n Off: 0'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# Main loop
while True:
    # Read an image ('img_2.png' in this case)
    img = cv2.imread('img_2.png', 1)

    # Get the current position of the 'CP' trackbar
    pos = cv2.getTrackbarPos('CP', 'image')

    # Define font and display the 'CP' trackbar value on the image
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, str(pos), (50, 20), font, 2, (0, 0, 255), 2)

    # Wait for a key event (1 millisecond)
    k = cv2.waitKey(1) & 0xFF

    # If the 'Esc' key is pressed, break out of the loop
    if k == 27:
        break

    # Get the current position of the switch trackbar
    s = cv2.getTrackbarPos(switch, 'image')

    # If the switch is turned off (0), do nothing; otherwise, convert the image to grayscale
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the resulting image
    img = cv2.imshow('image', img)

# Close all OpenCV windows
cv2.destroyAllWindows()
