#!/bin/bash
#Created by Rev.Raikes for use with the Sense Hat for Raspberry Pi 4

#Make directory and copy .py to /opt/sense-hat/ so that below script can find it
sudo mkdir -p /opt/sense-hat
sudo cp gauss_y_n_shutdown.py /opt/sense-hat/

#Copy shell script to binaries for systemd to use
sudo cp gauss-yns.sh /usr/local/bin/

#Create .service file in systemd folder
sudo cp gauss-yns.service /etc/systemd/system/ 

#Reload daemon system and set Python app to start on boot
sudo systemctl daemon-reload
sudo systemctl start gauss-yns.service
sudo systemctl enable gauss-yns.service
sudo systemctl status gauss-yns.service
