import json
import RPi.GPIO as GPIO
import Adafruit_DHT
from flask import Flask, request, Response
app = Flask(__name__)

# GPIO.setmode(GPIO.BCM)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi 3 with DHT11 sensor
# connected to GPIO17.
pin = 17

@app.route("/")
def main():
  # Try to grab a sensor reading.  Use the read_retry method which will retry up
  # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  
  templateData = {
      'humidity' : humidity,
      'temperature' : temperature
   }
  
  # Pass the template data into the template main.html and return it to the user
  return Response(json.dumps(templateData), mimetype='application/json')

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<action>")
def action(action):
   # If the action part of the URL is "temperature," execute the code indented below:
   # Try to grab a sensor reading.  Use the read_retry method which will retry up
   # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   
   if action == "temperature":
      action_result = temperature
   if action == "humidity":
      action_result = humidity

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      action : action_result
   }

   return Response(json.dumps(templateData), mimetype='application/json')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8989, debug=True)
