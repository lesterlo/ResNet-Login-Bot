# ResNet-auto-login

## Introuduction
This python script provide simple login script to the ResNet portal.

## Usage
First, input your username and password to login_config.py
Then, use resnet_login.py to login
```bash
python3 resnet_login.py
```



## Install
You can install a systemd daemon named resnet_login.service to the system. The daemon will check the login status each 30 min. You can change the checking frequency on exe_freq=30 on monitor_script.py
```bash
./install.sh
```


