from config import *
from camera import feed
from object_detection import object_detect
import time


if __name__ == "__main__":

    # camera index 0 - internal camera
    # camera index 2 - external camera (may need to change)
    camera_index = CONFIG_cam_index

    # open camera
    cap = feed.start(camera_index)

    # flag to see if timer is started
    f_timer_started = False

    while True:
        frame = feed.get(cap)

        top_class_index = object_detect.classify_image(frame)
        is_dog = object_detect.is_dog(top_class_index)

        if is_dog:
            if not f_timer_started:
                start_time = time.time()
                f_timer_started = True
            elapsed_time = int(time.time() - start_time)
            if elapsed_time > CONFIG_dog_potty_timeout_time_seconds:
                #generate alert
                print("Dog Potty Alert")
        else:
            f_timer_started = False

        if CONFIG_show_feed:
            text = f"{'DOG' if is_dog else '?'}"
            feed.show(frame,text)

        # Break the loop if the user presses the 'q' key
        if feed.is_quit_key_pressed():
            break
    # cleanup
    feed.exit(cap)
