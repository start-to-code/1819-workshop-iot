# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()

# Constants
BK = (0,0,0)
WH = (255,255,255)
RD = (255, 0, 77)
BL = (41, 173, 255)
BR = (187, 90, 59)
PK = (255, 208, 174)
YL = (250, 252, 44)

MARIO = [
    BK, BK, BK, RD, RD, RD, WH, BK,
    BK, BK, BK, RD, RD, RD, RD, RD,
    BK, BK, BR, PK, BR, BK, PK, BK,
    BK, BK, BR, PK, PK, BR, BR, PK,
    BK, BK, BK, BR, PK, PK, PK, BK,
    BK, RD, RD, YL, BL, BL, YL, BK,
    WH, BK, BL, BL, BL, BL, BK, BL,
    BK, BK, BR, BK, BK, BK, RD, BK  
    
]

MARIO_JUMP = [
    BK, BK, BK, RD, RD, RD, RD, RD,
    BK, BK, BR, PK, BR, BK, PK, BK,
    BK, BK, BR, PK, PK, BR, BR, PK,
    BK, BK, BK, BR, PK, PK, PK, BK,
    WH, RD, BL, YL, BL, BL, YL, BL,
    BK, BK, BR, BK, BK, BK, RD, BK,  
    BK, BK, BK, BK, BK, BK, BK, BK,   
    BK, BK, BK, BK, BK, BK, BK, BK    
]

jump = False
        
# Endless loop
while True:
    try:
        if jump:
          sense.set_pixels(MARIO_JUMP)
        else:
          sense.set_pixels(MARIO)
          
        sleep(1)
        
        jump = not jump
        sense.clear()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)