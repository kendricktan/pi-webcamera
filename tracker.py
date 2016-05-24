import numpy as np
import os
import sys
import cv2
import csv
import time
from time import gmtime, strftime

class Tracker(object):
    def __init__(self):
	# Camera parameters
        self.cap = cv2.VideoCapture(-1)
	self.cap.set(3, 320) # width
	self.cap.set(4, 240) # height

	# Pre-trained models
        self.face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
        self.body_cascade = cv2.CascadeClassifier('./xml/haarcascade_fullbody.xml')
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
	# Get frame
        ret, frame = self.cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Match against pre trained models
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = self.body_cascade.detectMultiScale(gray)

        # Draw faces and bodies
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0 ,0), 2)

        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0 ,0), 2)

	# Chuck to csv and save image if detects face
        if len(faces) is not 0 or len(bodies) is not 0:
            with open('./static/log.csv', 'r+') as f:
		# Save image
                c_time = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
                filename = c_time + '.jpg'
                cv2.imwrite(os.path.join('img', filename), frame)

		# CSV
                filename='<a href="img/'+filename+'">'+filename+'</a>'
                content = f.read()
                f.seek(0, 0)
                f.write(filename.rstrip('\r\n') + '\n' + content)

	# html compatible
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tostring()
