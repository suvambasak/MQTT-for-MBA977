# Pi Setup

### Virtual env
```bash
python3 -m venv .venv
```

```bash
. .venv/bin/activate
```
### Install packages

Either
```bash
pip3 install -r requirements.txt
```


Or
```bash
pip3 install spidev mfrc522
```

```bash
pip3 install paho-mqtt==1.6.1
```


### Reference
1. https://pimylifeup.com/raspberry-pi-rfid-rc522/
2. https://github.com/lthiery/SPI-Py.git