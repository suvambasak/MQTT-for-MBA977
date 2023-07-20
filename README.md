# Message Queuing Telemetry Transport (MQTT) cheat sheet


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
mosquitto_sub -h 172.27.22.238 -t "sensors/temp/bedroom"
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
mosquitto_pub -h 172.27.22.238 -t "sensors/temp/bedroom" -m "27.5"
```