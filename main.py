import cv2
from camera import feed

if __name__ == "__main__":
    # camera index 0 - internal camera
    # camera index 2 - external camera (may need to change)
    camera_index = 0

    # open camera
    cap = feed.capture_start(camera_index)

    # Load the pre-trained Haarcascade for dog detection
    dog_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        frame = feed.capture_get_feed(cap)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dogs = dog_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10)
        # Draw rectangles around detected dogs
        for (x, y, w, h) in dogs:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        feed.capture_show_feed(frame)
        # Break the loop if the user presses the 'q' key
        if feed.capture_quit_request():
            break
    # cleanup
    feed.capture_exit(cap)
