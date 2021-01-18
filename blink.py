· #Blink

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:

    GPIO.output(7, True)
    time.sleep(0.2)
    print("on")
    GPIO.output(7, False)
    time.sleep(0.2)
    print("off")