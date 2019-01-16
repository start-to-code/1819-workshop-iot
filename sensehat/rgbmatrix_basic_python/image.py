# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()
# Load image into the matrix
os.chdir(os.path.dirname(__file__))
dirpath = os.getcwd()
sense.load_image(dirpath + '/images/space_invader.png')

# Endless loop
while True:
    try:
        sleep(1)

    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)