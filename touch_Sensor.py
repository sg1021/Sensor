from time import sleep, time
import RPi.GPIO as GPIO

TOUCH_PORT = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PORT, GPIO.IN)

def touch():
    value = 0
    if GPIO.input(TOUCH_PORT):
        value = 1
    else:
        value = 0
    return value

try:
    while True:
        ans = touch()
        if ans == 1:
            print('Touch now!')
            sleep(1)
        else:
            sleep(0.1)

except KeyboardInterrupt:
    pass
GPIO.cleanup()