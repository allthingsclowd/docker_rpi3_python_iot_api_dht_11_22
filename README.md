# Raspberry Pi 3 IoT Demo using Docker &amp; Python 2.7 to read a DHT11 or DHT22 Temperature and Humidity Sensor using a RESTful API

The Dockerfile in this repo can be used to build an IoT demo container that runs a Python 2.7 application that will work with the GPIO pins configured to match the following setup :
![rpi3-dht11-dht22_bb](https://user-images.githubusercontent.com/9472095/37230251-ac0e8fba-23de-11e8-903f-b1987650cd0d.jpg)
![rpi3-dht11-dht22_schem](https://user-images.githubusercontent.com/9472095/37230255-afadce42-23de-11e8-841a-7d16a8be0285.jpg)


The docker image can be found here: https://hub.docker.com/r/allthingscloud/rpi3-python-iot-api-dht/


To build the dockerfile on a raspberry pi 3 after cloning this repository: 
```bash
docker image build --tag allthingscloud/rpi3-python-iot-api-dht -f Dockerfile . 
```

Launch as follows:
```bash
docker container run -d -p 4321:8989 --name my-python-iot-demo --device /dev/gpiomem allthingscloud/rpi3-python-iot-api-dht
```
# Verification
## Using curl
```bash
curl http://raspberry-pi-ip-address:4321/   <-- Returns both the temperature and the humidity readings in JSON format
						  
curl http://raspberry-pi-ip-address:4321/temperature   <-- Returns a JSON temperature response
						       
curl http://raspberry-pi-ip-address:4321/humidity   <-- Returns a JSON humidity response
```
							
							
## Using a browser
Navigate to :
```bash
http://raspberry-pi-ip-address:4321/   <-- Returns both the temperature and the humidity readings in JSON format
					     
http://raspberry-pi-ip-address:4321/17/on   <-- Returns a JSON temperature response
						  
http://raspberry-pi-ip-address:4321/17/off   <-- Returns a JSON humidity response
```


# Raspberry Pi 3 - Docker Installation
Please check the official documentation at https://docs.docker.com

I used the following steps :

```bash

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
	
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

echo "deb [arch=armhf] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list   
   
sudo apt-get update

sudo apt-get install docker-ce

```
