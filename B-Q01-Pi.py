#!/user/bin/python
import RPi.GPIO as GPIO         # Import Raspberry Pi GPIO library
from time import sleep          # Import the sleep function 

GPIO.setmode(GPIO.BCM)            # Specify GPIO numbers instead of pin numbers
led = 17

GPIO.setwarnings(True)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        GPIO.output(led, GPIO.HIGH)
        print("LED on")
        sleep(1)
        GPIO.output(led, GPIO.LOW)
        print("LED off")
        sleep(1)
finally:
    GPIO.cleanup()
