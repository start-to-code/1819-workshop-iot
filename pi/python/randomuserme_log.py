# Import the necessary libraries
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
from random import randint
import json
from urllib import request

api_url = 'https://randomuser.me/api/?results=10&format=json'
with request.urlopen(api_url) as response:
  data = json.loads(response.read().decode())

for index, human in enumerate(data['results']):
  print("""
  |=================================================================================|
  |                            User: %s                                              |
  |=================================================================================|
  | Name: \t\t%s %s %s
  | Gender: \t\t%s
  | Nationality: \t%s
  | Day of birth: \t%s
  | Location: \t\t%s, %s %s (%s)
  | Phone: \t\t%s
  | Cell: \t\t%s
  | Email: \t\t%s
  | Username: \t\t%s
  |=================================================================================|
  """ % (
    index,
    human['name']['title'].capitalize(),
    human['name']['first'].capitalize(),
    human['name']['last'].capitalize(),
    human['gender'],
    human['nat'],
    human['dob']['date'],
    human['location']['street'].capitalize(),
    human['location']['postcode'],
    human['location']['city'].capitalize(),
    human['location']['state'].capitalize(),
    human['phone'],
    human['cell'],
    human['email'],
    human['login']['username'],
    )
  )