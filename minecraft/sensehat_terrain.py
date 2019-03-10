# Import libraries
import mcpi.minecraft as minecraft
from sense_hat import SenseHat
from time import sleep
import os
import sys

# Connect the SenseHat
try:
  sense = SenseHat()
  sense.clear()
except:
  print('You have to connect the SenseHat in a propper way!')
  sys.exit(0)

# Connect Minecraft
try:
  mc = minecraft.Minecraft.create()
  mc.postToChat('Hello Minecraft! Greetings from NMD')
except:
  print('You have to start minecraft!')
  sys.exit(0)

# Constants
blocks = {
  0: {
    'label': 'Air',
    'color': (0,0,255)
  },
  1: {
    'label': 'Stone',
    'color': (0,0,255)
  },
  2: {
    'label': 'Grass',
    'color': (0,255,0)
  },
  3: {
    'label': 'Dirt',
    'color': (0,255,0)
  },
  8: {
    'label': 'Water',
    'color': (0,255,0)
  },
  12: {
    'label': 'Sand',
    'color': (255,255,255)
  },
  79: {
    'label': 'Ice',
    'color': (255,255,255)
  }
}

# Endless loop
while True:
    try:
        x, y, z = mc.player.getTilePos()
        block = mc.getBlock(x, y-1, z)
        if block in blocks:
          print(block)
          sense.clear(blocks[block]['color'])
        else:
          print(block)
          sense.clear()
        sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)