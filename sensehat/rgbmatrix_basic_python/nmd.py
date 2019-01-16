# Import the necessary libraries
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint

# constants
TEXT = 'NMD'

# function: get random color()
def get_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)

    return (random_red, random_green, random_blue)

# Make an instance of SenseHat
sense = SenseHat()

# Endless loop
while True:
    try:
        for letter in TEXT:
            sense.show_letter(letter, get_random_color())
            sleep(1)
        sleep(2)
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)