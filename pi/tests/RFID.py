import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:

    while True:
        id, text = reader.read()
        print(f"ID: {id}\tText:{text}")

        time.sleep(1)

except KeyboardInterrupt as e:
    print('\n Stopped.\n')
finally:
    GPIO.cleanup()
