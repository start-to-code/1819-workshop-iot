# Import the necessary libraries
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint

# Constants
M_ROWS = 7
M_COLS = 7
M_CLEAR_BEFORE_LOOP = True

# function: get_random_color()
def get_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)

    return (random_red, random_green, random_blue)

# Make an instance of SenseHat
sense = SenseHat()
sense.set_imu_config(False, False, False)
    
# Endless loop
while True:
    try:
        x_pos = 0
        y_pos = 0

        while (y_pos <= M_ROWS):
            if M_CLEAR_BEFORE_LOOP:
                sense.clear()
                
            sense.set_pixel(x_pos, y_pos, get_random_color())
            sleep(0.1)
            
            y_pos = (y_pos + 1) if (x_pos + 1 == M_COLS + 1) else (y_pos)
            x_pos = (x_pos + 1) if (x_pos + 1 <= M_COLS) else (0)

        sleep(2)
        sense.clear()

    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)