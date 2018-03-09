FROM arm32v7/python:2.7.14-stretch

RUN apt-get update && \
apt-get install -y git python-flask && \
pip install flask && \
git clone https://github.com/adafruit/Adafruit_Python_DHT.git

WORKDIR Adafruit_Python_DHT

RUN python setup.py install && \
git clone https://github.com/allthingsclowd/docker_rpi3_python_iot_api_dht_11_22.git

WORKDIR /docker_rpi3_python_iot_api_dht_11_22

EXPOSE 8989

CMD python api-to-read-dht11-dht22.py
