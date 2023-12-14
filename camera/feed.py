import cv2

def capture_start(camera):
    cap = cv2.VideoCapture(camera)
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return -1
    else:
        return cap

def capture_feed_loop(camera):
    # Read a frame from the camera
    ret, frame = camera.read()
    # If the frame was not read successfully, break the loop
    if not ret:
        print("Error: Could not read frame.")
    # Display the frame
    cv2.imshow("Webcam Feed", frame)

def capture_quit_request():
    return cv2.waitKey(1) & 0xFF == ord('q')

def capture_exit(camera):
    camera.release()
    cv2.destroyAllWindows()
