from picamera import PiCamera
import time
import datetime
import requests
import os

camera = PiCamera() 


ec2url1 = "http://ec2-3-87-237-187.compute-1.amazonaws.com:8081/giveFrame"
# ec2url2 = "http://ec2-18-212-88-34.compute-1.amazonaws.com:8081/healthCheck"


# requests.get(ec2url2)
camera.start_preview()


fileName = str(datetime.datetime.now()).replace(" ", "+")
filePath = '/home/pi/testImages/' + fileName + '.jpg'
camera.capture(filePath)

print(filePath)

frame = {'image': open(filePath, 'rb')}

requests.post(ec2url1, files=frame, data={'timestamp': fileName})

os.remove(filePath) #cleanup

camera.stop_preview()