#!/user/bin/python
import RPi.GPIO as GPIO         # Import Raspberry Pi GPIO library
from time import sleep          # Import the sleep function 

GPIO.setmode(GPIO.BCM)            # Specify GPIO numbers instead of pin numbers
rPin = 17
gPin = 27
bPin = 22

GPIO.setwarnings(True)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

def turnOff():
    GPIO.output(rPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)

def white():
    GPIO.output(rPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.HIGH)
    GPIO.output(bPin, GPIO.HIGH)

def red():
    GPIO.output(rPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)

def green():
    GPIO.output(rPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.HIGH)
    GPIO.output(bPin, GPIO.LOW)

def blue():
    GPIO.output(rPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.HIGH)

try:
    while True:
        turnOff()
        print("LED off")
        sleep(1)
        red()
        print("LED red")
        sleep(1)
        green()
        print("LED green")
        sleep(1)
        blue()
        print("LED blue")
        sleep(1)
finally:
    turnOff()
    GPIO.cleanup()

