import cv2
""" Setting Camera Parameters in OpenCV Python """
# Initialize video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Print the current frame width and height
print("Current frame width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Current frame height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set desired frame width and height
cap.set(3, 1208)  # Width
cap.set(4, 720)   # Height

# Print the updated frame width and height
print("Updated frame width:", cap.get(3))
print("Updated frame height:", cap.get(4))

while cap.isOpened():
    # Read a frame from the camera
    ret, frame = cap.read()
    
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display the grayscale frame in a window named 'vid'
        cv2.imshow('vid', gray)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error opening camera or no frame received")
        break

# Release the video capture resources
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
