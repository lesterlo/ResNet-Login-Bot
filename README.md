# CUHK ResNet Login Bot

## Introduction
This python script keeps the CUHK ResNet or WiFi connection persistently. By default, the CUHK ResNet/WiFi has 8 hours timeout on each session. This login Bot can check the network connection status and re-login the CUHK ResNet/WiFi automatically after the 8 hours timeout.

No network service interruption in your hostel room anymore. :)

If you have Home Assistant on Raspberry Pi, please use the [CUHK ResNet Login Service in Home Assistant](https://github.com/lesterlo/ResNet-Login-hass).


## Usage
For one-time login.

First, modify your username and password on login_config.py

Then, use resnet_login.py to login

```bash
python3 resnet_login.py
```

## Installation

For keeping the network alive.

You can install a systemd daemon named resnet_login.service to your system. The daemon will check the login status every 30 min by default. You can change the checking frequency on login_freq=30 on login_config.py


```bash
./install.sh
```

## Uninstall the Bot

To uninstall the login bot, simply run the uninstall script.

```bash
./uninstall.sh
```

## Troubleshooting
#### 1. No module named request
Please install the requests module with pip
```bash
sudo pip3 install requests
```

#### 2. No User name pi
Please modify the user account name to something in **resnet_login.service** on **Line 7**
```bash
[Service]
User=<Your_Username>
```

## Reference
https://github.com/SaneBow/ResNetAutoLogin
