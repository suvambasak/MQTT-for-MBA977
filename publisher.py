import random
import time

import paho.mqtt.client as paho

# Connection details
HOST = "localhost"
PORT = 1883
TIME_OUT = 60

# Topic and data
TOPIC = "sensors/temp/bedroom"


# Create connection
client = paho.Client()
if client.connect(HOST, PORT, TIME_OUT):
    print('Connection failed!')
    exit(-1)


try:
    while True:
        temp = random.random() * 100

        # Publish to the topic
        client.publish(
            TOPIC,
            temp,
            0
        )

        time.sleep(1)

except KeyboardInterrupt as e:
    print('\nSTOP : Publisher service.\n')
finally:
    client.disconnect()
