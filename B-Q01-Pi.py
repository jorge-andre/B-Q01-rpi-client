#!/user/bin/python
# import RPi.GPIO as GPIO
from time import sleep
from confluent_kafka import Consumer, KafkaException
import json
from threading import Thread
import queue

# GPIO.setmode(GPIO.BCM)            # Specify GPIO numbers instead of pin numbers
rPin = 17
gPin = 27
bPin = 22

# GPIO.setwarnings(True)
# GPIO.setup(rPin, GPIO.OUT)
# GPIO.setup(gPin, GPIO.OUT)
# GPIO.setup(bPin, GPIO.OUT)

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

def kafkaWorker():
    conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'foo',
        'auto.offset.reset': 'smallest'}
    consumer = Consumer(conf)

    try:
        consumer.subscribe(['departures'])

        while True:
            msg = consumer.poll()
            if msg is None:
                print('No messages to read.')
                continue
            if msg.error():
                raise KafkaException(msg.error)
            
            arrival = json.loads(msg.value())
            arrivalQueue.put(arrival)
            break
    finally:
        consumer.close()

arrivalQueue = queue.Queue()
Thread(target=kafkaWorker, daemon=True).start()

while True:
    arrival = arrivalQueue.get_nowait()