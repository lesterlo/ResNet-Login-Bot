sudo systemctl stop resnet_login.service

sudo systemctl disable resnet_login.service
sudo systemctl daemon-reload
sudo rm /etc/systemd/system/resnet_login.service

sudo rm -rf /opt/resnet_login
