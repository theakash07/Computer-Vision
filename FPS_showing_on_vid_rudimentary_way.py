import cv2
import time

cap = cv2.VideoCapture('pinterestvid.mp4')

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1208)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

# Initialize prev_frame_time
prev_frame_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f'Width: {cap.get(3)}, Height: {cap.get(4)}'
        frame = cv2.putText(frame, text, (17, 45), font, 1, (0, 24, 89), 3, cv2.LINE_AA)

        # Calculate FPS
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps_text = f'FPS: {fps}'
        frame = cv2.putText(frame, fps_text, (17, 80), font, 1, (0, 24, 89), 3, cv2.LINE_AA)

        cv2.imshow('pinterestvid.mp4', frame)

        if cv2.waitKey(5000) & 0xFF == ord('q'):
            break
    else:
        print("Error opening video")
        break

cap.release()
cv2.destroyAllWindows()
