#!/user/bin/python
# import RPi.GPIO as GPIO
from time import sleep
from confluent_kafka import Consumer, KafkaException
import json

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


# consumer = KafkaConsumer('departures',
#                          bootstrap_servers=['localhost:9092'],
#                          client_id='rpi-zero-python',
#                          value_deserializer=lambda m: json.loads(m.decode('utf8')))
# while True:
#     print('polling kafka')
#     messages = consumer.poll()
#     print(messages)
#     for message in messages['departures']:
#         print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                               message.offset, message.key,
#                                               message.value))
#         arrivalTime = message.value["rtTime"]
#         direction = message.value["direction"]
#         print("time:%s  direction:%s" % (arrivalTime, direction))
#         nextDeparture = message.value

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
        if msg.error():
            raise KafkaException(msg.error)
        
        print(msg.value())
        break
finally:
    consumer.close()