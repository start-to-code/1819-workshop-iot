# Import the necessary libraries
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint

# Constants
TEXT = 'Hello! We are New Media Development :)'
SPEED = 0.1

# function: get_random_color()
def get_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)

    return (random_red, random_green, random_blue)

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()

# Endless loop
while True:
    try:
        sense.show_message(text_string=TEXT, text_colour=get_random_color(), back_colour=get_random_color(), scroll_speed=SPEED)
        sense.clear()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)