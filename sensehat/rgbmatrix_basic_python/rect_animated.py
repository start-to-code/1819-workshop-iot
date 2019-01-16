# Import the necessary libraries
from sense_hat import SenseHat
import random
from math import floor, ceil
import time
import sys
import os

# class: MatrixRect
class MatrixRect:

    def __init__(self, w, h, ledc_on, filled):
        self.matrix = []
        self.ledc_black = (0, 0, 0)
        self.ledc_on = ledc_on
        self.w = w
        self.h = h
        self.filled = filled
        self.createBlackMatrix();
        self.createPattern()

    def createBlackMatrix(self):
        for p in range(0,64):
            self.matrix.append(self.ledc_black)

    def createPattern(self):
        for r in range(0,self.w):
            for c in range(0, self.h):
                if self.filled == False:
                    ledc = self.ledc_black
                    if r == 0 or (r == self.w - 1):
                        ledc = self.ledc_on
                    elif c == 0 or c == self.h - 1:
                        ledc = self.ledc_on

                    self.matrix[r*8+c] = ledc
                else:
                    self.matrix[r*8+c] = ledc_on

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()

# Constants
i = 0
dir = 1
ledc_on = (255, 0, 0)

# Endless loop
while True:
    try:
        m = MatrixRect(i, i, ledc_on, False)
        sense.set_pixels(m.matrix)

        temp_i = i+1*dir
        if temp_i <= 8 and temp_i >= 0:
            i = temp_i
        else:
            ledc_on = (round(random.random()*255), round(random.random()*255), round(random.random()*255))
            dir = dir*-1

        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)