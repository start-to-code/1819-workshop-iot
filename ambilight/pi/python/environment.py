'''
Start to Code
=============
Workshop: Internet of Things (IoT)
Application: Ambilight
--------------------------------------
Author: Philippe De Pauw - Waterschoot
Opleiding: Grafische en digitale media
Specialisatie: New Media Development
'''

# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os
from google.cloud import firestore

# Constants
COLLECTION_NAME = u'pis'
PI_ID = u'stc_pi_1'

# Make an instance of SenseHat
sense = SenseHat()
# Clear the RGB matrix
sense.clear()

# Initalize Firebase
# Use the service account for own server
os.chdir(os.path.dirname(__file__))
dirpath = os.getcwd()
db = firestore.Client.from_service_account_json(dirpath + '/config/start-to-code-70340204ea7b.json')

# function: on_snapshot(doc_snapshot, changes, read_time)

# Get the pi environment ref
pi_ref = db.collection(COLLECTION_NAME).document(PI_ID)

while True:
    try:
        environmentObj = {
            u'temperature': {
                u'value': round(sense.get_temperature(),1),
                u'unit_code': u'C',
                u'unit_text': u'Celcius'
            },
            u'humidity': {
                u'value': sense.get_humidity(),
                u'unit_code': u'%',
                u'unit_text': u'Percentage'
            },
            u'pressure': {
                u'value': sense.get_pressure(),
                u'unit_code': u'mBar',
                u'unit_text': u'Milli Bar'
            }
        }
        pi_ref.set({ 'environment': environmentObj }, merge=True )

        sleep(60)

    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sense.clear()
        sys.exit(0)