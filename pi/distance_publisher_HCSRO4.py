import time

import paho.mqtt.client as paho
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Connection details
HOST = "172.27.28.18"
PORT = 1883
TIME_OUT = 60

# Topic and data
TOPIC = "sensors/dist_cm"

# Pin setup
TRIG = 26
ECHO = 21
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


# Create connection
client = paho.Client()
if client.connect(HOST, PORT, TIME_OUT):
    print('Connection failed!')
    exit(-1)


try:
    while True:
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == False:
            start = time.time()

        while GPIO.input(ECHO) == True:
            end = time.time()

        sig_time = end-start

        # cm:
        distance = sig_time / 0.000058

        # inches:
        # distance = sig_time / 0.000148

        print('Distance : {} cm'.format(distance))

        # Publish to the topic
        client.publish(
            TOPIC,
            distance,
            0
        )

except KeyboardInterrupt as e:
    print('\nSTOP : Publisher service.\n')
finally:
    client.disconnect()
    GPIO.cleanup()
