import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
from flask import Flask, request, Response

app = Flask(__name__)

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

@app.route("/")
def main():

  result = instance.read()

  if result.is_valid():
    templateData = {
        'humidity' : result.humidity,
        'temperature' : result.temperature
    }
  else:
    templateData = { 'empty' }

  # Pass the template data into the template main.html and return it to the user
  return Response(json.dumps(templateData), mimetype='application/json')

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<action>")
def action(action):
   # If the action part of the URL is "temperature," execute the code indented below:

  result = instance.read()
  action_result = 'empty'
  if result.is_valid():
    if action == "temperature":
      action_result = result.temperature
    if action == "humidity":
      action_result = result.humidity

   # Along with the pin dictionary, put the message into the template data dictionary:
  templateData = {
    action : action_result
  }

  return Response(json.dumps(templateData), mimetype='application/json')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8989, debug=True)
