# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os

# Make an instance of SenseHat
sense = SenseHat()

# Endless loop
while True:
  try:
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    temp_from_humidity = sense.get_temperature_from_humidity()
    temp_from_pressure = sense.get_temperature_from_pressure();
    pressure = sense.get_pressure()

    print("Humidity: %s %%" % humidity)
    print("Temperature: %s C" % temp)
    print("Temperature from humidity: %s C" % temp_from_humidity)
    print("Temperature from pressure: %s C" % temp_from_pressure)
    print("Pressure: %s Millibars" % pressure)

    sleep(10)
  except KeyboardInterrupt:
    print('End of application')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)