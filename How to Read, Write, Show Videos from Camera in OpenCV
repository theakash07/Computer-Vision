import cv2
""" How to Read, Write, Show Videos from Camera in OpenCV """

"""Here video capture can be used as to just read the video file and give argument it to name of file"""
"""cap = cv2.VideoCapture('Video filename.format')"""
#by default two argument either 0 or -1 for device camera
cap = cv2.VideoCapture(0)
#if video capture giving error it will return false so cap will become false.
print(cap.isOpened())
"""fourcc is used for video encoder it provides the file format of video"""
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    #read method going to return true if frame is available and the frame going to save in frame variable
    #ret is for true and false if frame available it will be true else it wll be false
    ret, frame = cap.read()
    out.write(frame)
    # Check if frame read was successful
    if not ret:
        print("Error reading frame. Exiting loop.")
        break

    """To get the details of frame width and height"""
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #below code is used to convert the bgr( 3 channel) into grayscale ( 1 channel ) .
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Working")
        break


#after using each methods release it
cap.release() 
out.release()
cv2.destroyAllWindows()






