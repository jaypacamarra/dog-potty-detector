from camera import feed

if __name__ == "__main__":
    # open camera
    # camera index 2 (may need to change)
    cap = feed.capture_start(2)
    while True:
        feed.capture_feed_loop(cap)
        # Break the loop if the user presses the 'q' key
        if feed.capture_quit_request():
            break
    # cleanup
    feed.capture_exit(cap)
