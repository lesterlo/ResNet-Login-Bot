sudo systemctl stop resnet_login.service

sudo mkdir -p /opt/resnet_login && sudo cp * /opt/resnet_login
sudo cp resnet_login.service /etc/systemd/system
sudo chmod +x /opt/resnet_login/monitor_script.py

sudo systemctl enable resnet_login.service
sudo systemctl daemon-reload
sudo systemctl start resnet_login.service
sudo systemctl status resnet_login.service
