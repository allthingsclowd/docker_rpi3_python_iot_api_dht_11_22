FROM arm32v7/python:2.7.14-stretch

RUN apt-get update && \
apt-get install -y git python-flask && \
pip install flask && \
git clone https://github.com/allthingsclowd/DHT11_Python.git

WORKDIR DHT11_Python

RUN git clone https://github.com/allthingsclowd/docker_rpi3_python_iot_api_dht_11_22.git .

EXPOSE 8989

CMD python api-to-read-dht11-dht22.py
