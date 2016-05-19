# pi-webcamera
Web interface to monitor camera feed from Raspberry Pi

![web ui](http://i.imgur.com/7nW8lhz.png)

# Getting-started

1. Dependencies

	sudo apt-get install python python-pip python-opencv
	sudo pip install flask

2. Extract and run webcam server

	cd ~
	git clone https://github.com:kendricktan/pi-webcamera.git
	cd pi-webcamera
	python server.py

Navigate to http://your-ip-address:5000
