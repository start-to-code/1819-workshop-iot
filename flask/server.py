'''
Installation: 
sudo pip install -U Flask
sudo pip3 install -U Flask
Documentation:
http://flask.pocoo.org/
'''

# Import libraries
from flask import Flask, jsonify, render_template, request, url_for
from sense_hat import SenseHat
from time import sleep
import sys
import os

# Initiate Flask
app = Flask(__name__)

# Make an instance of SenseHat
sense = SenseHat()

# Routes
@app.route('/')
def index():
    return "Looks like it works!"

@app.route('/nmd')
def nmd():
    return "Greetings Earthlings! Welcome to the NMD-hotspot :)"

@app.route("/my_ip", methods=["GET"])
def get_my_ip():
    return jsonify(
      {
        'ip': request.remote_addr
      }), 200

# Route with template returning (using Ninja2 templating system)
@app.route("/environment", methods=["GET"])
def get_environment():
    json_obj = {
        'temperature': {
          'value': round(sense.get_temperature()),
          'unit': u'°C'
        },
        'humidity': {
          'value': round(sense.get_humidity()),
          'unit': u'%'
        },
        'pressure': {
          'value': round(sense.get_pressure()),
          'unit': u'mbar'
        }
    }
    return render_template('environment.html', environment=json_obj)

@app.route("/api/environment", methods=["GET"])
def api_get_environment():
    return jsonify(
      {
        'temperature': {
          'value': round(sense.get_temperature()),
          'unit': u'°C'
        },
        'humidity': {
          'value': round(sense.get_humidity()),
          'unit': u'%'
        },
        'pressure': {
          'value': round(sense.get_pressure()),
          'unit': u'mbar'
        }
      }), 200

@app.route('/api/ambilight/<string:id>', methods=['POST'])
def api_update_ambilight(id):
    content = request.json
    print(content)
    return jsonify({"uuid":id})

# Test all the urls
with app.test_request_context():
    print(url_for('index'))
    print(url_for('nmd'))
    print(url_for('api_get_environment'))

# Main method for Flask
if __name__ == '__main__':
    app.run(host = '192.168.0.8', port=8080, debug=True)