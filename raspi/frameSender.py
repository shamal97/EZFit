from picamera import PiCamera
import time
import datetime
import requests
import os

camera = PiCamera() 


ec2url1 = "http://ec2-52-20-94-253.compute-1.amazonaws.com:8081/giveFrame"

camera.start_preview()

while True:    
    time.sleep(.25)
    fileName = str(datetime.datetime.now()).replace(" ", "+")
    filePath = '/home/pi/testImages/' + fileName + '.jpg'
    camera.capture(filePath)
    print(filePath)
    frame = {'image': open(filePath, 'rb')}
    requests.post(ec2url1, files=frame, data={'timestamp': fileName})

    os.remove(filePath) #cleanup

camera.stop_preview()