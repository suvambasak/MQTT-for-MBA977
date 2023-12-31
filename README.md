# MQTT Cheat Sheet

## Table of Contents
- [MQTT CLI](#install-mqtt-broker-and-client)
    - [Broker setup](#broker-setup) 
    - [Client setup](#client-setup)
- [MQTT Automation with Python](#automation-with-python-scripts)
    - [Setup](#setup)
    - [Publisher script](#publisher)
    - [Subscriber script](#subscriber)
    - [Visualization from live stream](#visualization-from-live-stream)


## Install MQTT Broker and Client
- Install two package: `mosquitto` and `mosquitto-clients`
```bash
sudo apt install mosquitto mosquitto-clients
```

## Broker setup
- Enable the broker service
```bash
sudo systemctl enable mosquitto
```
- Check the status of the service
```bash
sudo systemctl status mosquitto
```
### Enable the service in LAN
- Change the config file
```bash
sudo nano /etc/mosquitto/mosquitto.conf
```
```bash
allow_anonymous true
listener 1883
```
- Restart the service
```bash
sudo systemctl restart mosquitto
```


## Client setup
### Subscribe
```bash
mosquitto_sub -h localhost -t "sensors/temp/bedroom"
```
```bash
mosquitto_sub -h localhost -t "sensors/temp/livingroom"
```
### Subscribe over LAN
```bash
mosquitto_sub -h 172.27.28.217 -t "sensors/temp/bedroom"
```

### Publish
```bash
mosquitto_pub -h localhost -t "sensors/temp/bedroom" -m "27.5"
```
```bash
mosquitto_pub -h localhost -t "sensors/temp/livingroom" -m "24"
```
### Publish over LAN
```bash
mosquitto_pub -h 172.27.28.217 -t "sensors/temp/bedroom" -m "27.5"
```

## Automation with python scripts

### Setup
```bash
pip install -r requirements.txt
```
```python
# Connection details
HOST = "localhost"
PORT = 1883
TIME_OUT = 60

# Topic and data
TOPIC = "sensors/temp/bedroom"
```

### Publisher
Execute the `publisher.py` script
```bash
python publisher.py
```

### Subscriber
Execute the `subscriber.py` script
```bash
python subscriber.py
```

### Visualization from Live Stream
Execute publisher script `distance_publisher.py` script
```bash
python distance_publisher.py
```
Execute subscriber script `distance_live.py` script
```bash
python distance_live.py
```

<img src="/docs/output.gif">