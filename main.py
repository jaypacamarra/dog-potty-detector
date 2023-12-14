from camera import feed

if __name__ == "__main__":
    # open camera
    # camera index 2 (may need to change)
    cap = feed.capture_start(2)
    while True:
        frame = feed.capture_get_feed(cap)
        feed.capture_show_feed(frame)
        # Break the loop if the user presses the 'q' key
        if feed.capture_quit_request():
            break
    # cleanup
    feed.capture_exit(cap)
