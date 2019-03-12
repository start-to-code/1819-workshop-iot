'''
Installation: sudo pip3 install RPi.GPIO
'''

import RPi.GPIO as GPIO
import time
import os
import sys

# Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
channel_list = [17, 18] 
GPIO.setup(channel_list, GPIO.OUT)

while True:
  try:
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    # or GPIO.output(channel_list, (GPIO.HIGH, GPIO.LOW))
    time.sleep(0.2)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    # or GPIO.output(channel_list, (GPIO.LOW, GPIO.HIGH))
    time.sleep(0.2)

  except KeyboardInterrupt:
    print('End of application')
    try:
        GPIO.cleanup(channel_list)
        sys.exit(0)
    except SystemExit:
        os._exit(0)