import paho.mqtt.client as paho

# Connection details
HOST = "localhost"
PORT = 1883
TIME_OUT = 60


# Topic and data
TOPIC = "sensors/temp/bedroom"


def message_handler(client, user_data, msg):
    'Message handler'
    print(f'{msg.topic} : {msg.payload.decode()}')


# Create connection and register handler
client = paho.Client()
client.on_message = message_handler
if client.connect(HOST, PORT, TIME_OUT):
    print('Connection failed!')
    exit(-1)

# Subscribe to the topic
client.subscribe(TOPIC)
try:
    client.loop_forever()

except KeyboardInterrupt as e:
    print('\nSTOP: Subscriber service.\n')
finally:
    client.disconnect()
