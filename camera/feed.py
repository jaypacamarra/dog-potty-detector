import cv2

def start(camera):
    cap = cv2.VideoCapture(camera)
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return -1
    else:
        return cap

def get(camera):
    # Read a frame from the camera
    ret, frame = camera.read()
    # If the frame was not read successfully, break the loop
    if not ret:
        print("Error: Could not read frame.")
    return frame

def show(frame, text=""):
    if text != "":
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Feed', frame)

def is_quit_key_pressed():
    return cv2.waitKey(1) & 0xFF == ord('q')

def exit(camera):
    camera.release()
    cv2.destroyAllWindows()
