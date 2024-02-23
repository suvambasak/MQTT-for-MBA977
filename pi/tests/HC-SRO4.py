import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


TRIG = 26
ECHO = 21
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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


except KeyboardInterrupt as e:
    print('\n Stopped.\n')
finally:
    GPIO.cleanup()
