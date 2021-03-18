# CUHK ResNet Login Bot

## Introuduction
This python script provides a simple login procedure to login the CUHK ResNet portal. The login daemon can check the connection status and login the Resnet portal with your account automatically.

## Usage
For one time login.

First, modify your username and password on login_config.py

Then, use resnet_login.py to login

```bash
python3 resnet_login.py
```

### Windows user

> [Prerequisite] You need to have [Python](https://www.python.org/) installed, and added to [PATH](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows) variable in Windows.

First, modify your username and password on login_config.py.

Then, use windows.bat to login.

```cmd
windows.bat
```

## Installation

For keeping the network alive.

You can install a systemd daemon named resnet_login.service to your system. The daemon will check the login status for every 30 min by default. You can change the checking frequency on login_freq=30 on login_config.py


```bash
./install.sh
```

### Windows user

For keeping the network alive.

Add windows.bat to the [Task Scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10). Adjust the setting such that windows.bat is ran within every 12 hours to ensure the network keep alive.

## Uninstall the Bot

To uninstall the login bot, simply run the uninstall script.

```bash
./uninstall.sh
```

### Windows user

Remove the task in the Task Scheduler.

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
