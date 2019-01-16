# Import the necessary libraries
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil

# Constants
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# function: get_random_avatar_matrix()
def get_random_avatar_matrix():
    pattern = ''
    matrix = []
    for r in range(0,8):
        temp_str = ''
        for c in range(0, 4):
            temp_str = temp_str + str(round(random.random()))

        temp_str = temp_str + temp_str[::-1]
        pattern = pattern + temp_str                   
                    
    for p in range(0,64):
        bit = int(pattern[p])
        color = COLOR_BLUE if bit == 1 else COLOR_BLACK
        matrix.append(color)

    return(matrix)

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()

# Endless loop
while True:
    try:
        matrix = get_random_avatar_matrix();
        sense.set_pixels(matrix)
        sleep(3)
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)
