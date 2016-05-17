import numpy as np
import os
import sys
import cv2
import csv
import time
from time import gmtime, strftime

# Cascade classifiers
class Tracker:

    def __init__(self):
        # Camera parameters
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640) # Set width
        self.cap.set(4, 480) # Set height

        # Pre-trained models
        self.face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
        self.body_cascade = cv2.CascadeClassifier('./xml/haarcascade_fullbody.xml')

    def pipe_frame(self):
        # Capture frame
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

        # Chuck to csv and save image
        if faces is not None or bodies is not None:
            with open('./log.csv', 'a') as f:
                c_time = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
                filename = c_time + '.jpg'
                cv2.imwrite(os.path.join('img', filename), frame)
                writer= csv.writer(f, delimiter=';', lineterminator='\n') 
                filename='<a href=/img/'+filename+'>'+filename+'</a>'
                writer.writerow([filename])

        cv2.imwrite(os.path.join('img', 'frame.jpg'), frame)

tracker = Tracker()

while True:
    tracker.pipe_frame()
    time.sleep(1)
