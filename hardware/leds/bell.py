'''
Installation: sudo pip3 install RPi.GPIO
'''

import RPi.GPIO as GPIO
import time
import os
import sys

# Variables
input_channel = 16

# Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(input_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(input_channel, GPIO.RISING, bouncetime=500)


while True:
  try:
    if GPIO.event_detected(input_channel):
      print('Button pressed')
    pass

  except KeyboardInterrupt:
    print('End of application')
    try:
        GPIO.cleanup()
        sys.exit(0)
    except SystemExit:
        os._exit(0)