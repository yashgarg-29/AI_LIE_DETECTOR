#Start webcam
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from webcam
    if not ret:
        break

    cv2.imshow("Webcam", frame)  # Show the video in a window

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()