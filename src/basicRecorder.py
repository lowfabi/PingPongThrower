import cv2

# The index for /dev/video2 might vary. (in this case time its video2)
video_index = 2

# Start capturing video 
cap = cv2.VideoCapture(video_index)
if not cap.isOpened():
    print(f"Error: Could not open video device /dev/video{video_index}")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
