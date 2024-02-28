import os
import time
import RPi.GPIO as GPIO
from pushbullet import Pushbullet

TIMEOUT = 10

if __name__ == "__main__":
    pb = Pushbullet(os.environ["PUSHBULLET_API_KEY"])

    PIR = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR, GPIO.IN)

    timeout_sec = TIMEOUT
    notified = False
    wait = 5

    while True:
        if GPIO.input(PIR):
            time.sleep(wait)
            timeout_sec = timeout_sec - wait
            if timeout_sec:
                if GPIO.input(PIR):
                    if not notified:
                        pb.push_note("Doggo Detected", "Doggo needs to potty")
                        notified = True
            else:
                # reset flags after timeout_sec so we can send notifications again
                notified = False
                timeout_sec = TIMEOUT


