import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

IR = 20
GPIO.setup(IR, GPIO.IN)

try:
    while True:

        if GPIO.input(IR):
            sys.stdout.write(f'\r [IR sensor] No object       ')
        if not GPIO.input(IR):
            sys.stdout.write(f'\r [IR sensor] Object detected!')
        time.sleep(0.3)

except KeyboardInterrupt as e:
    print('\n Stopped.\n')
finally:
    GPIO.cleanup()
