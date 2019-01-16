# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os

# Make an instance of SenseHat
sense = SenseHat()
# Compass, gyroscope and accelerometer enabled
sense.set_imu_config(True, True, True)  

# Endless loop
while True:
  try:
    orientation_rad = sense.get_orientation_radians()
    orientation_deg = sense.get_orientation_degrees()

    print("Orientation (rad): p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))
    print("Orientation (deg): p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg))

    sleep(0.1)
  except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)