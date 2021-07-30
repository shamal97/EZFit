from picamera import PiCamera
import time
import datetime
import requests
import os

camera = PiCamera() 

ec2url1 = "http://ec2-3-89-114-79.compute-1.amazonaws.com:8081/giveFrame"

waitTime = 0.25 

time.sleep(2) #allow for me to go and walk infront of camera 



camera.start_preview()

fileName1 = str(datetime.datetime.now()).replace(" ", "+")
filePath1 = '/home/pi/testImages/' + fileName1 + '.jpg'
camera.capture(filePath1)
print(filePath1)
frame1 = ('image', open(filePath1, 'rb'))
time.sleep(waitTime)

fileName2 = str(datetime.datetime.now()).replace(" ", "+")
filePath2 = '/home/pi/testImages/' + fileName2 + '.jpg'
camera.capture(filePath2)
print(filePath2)
frame2 = ('image', open(filePath2, 'rb'))
time.sleep(waitTime)

fileName3 = str(datetime.datetime.now()).replace(" ", "+")
filePath3 = '/home/pi/testImages/' + fileName3 + '.jpg'
camera.capture(filePath3)
print(filePath3)
frame3 = ('image', open(filePath3, 'rb'))
time.sleep(waitTime)

fileName4 = str(datetime.datetime.now()).replace(" ", "+")
filePath4 = '/home/pi/testImages/' + fileName4 + '.jpg'
camera.capture(filePath4)
print(filePath4)
frame4 = ('image', open(filePath4, 'rb'))
time.sleep(waitTime)






fileName5 = str(datetime.datetime.now()).replace(" ", "+")
filePath5 = '/home/pi/testImages/' + fileName5 + '.jpg'
camera.capture(filePath5)
print(filePath5)
frame5 = ('image', open(filePath5, 'rb'))
time.sleep(waitTime)

fileName6 = str(datetime.datetime.now()).replace(" ", "+")
filePath6 = '/home/pi/testImages/' + fileName6 + '.jpg'
camera.capture(filePath6)
print(filePath6)
frame6 = ('image', open(filePath6, 'rb'))
time.sleep(waitTime)

fileName7 = str(datetime.datetime.now()).replace(" ", "+")
filePath7 = '/home/pi/testImages/' + fileName7 + '.jpg'
camera.capture(filePath7)
print(filePath7)
frame7 = ('image', open(filePath7, 'rb'))
time.sleep(waitTime)

fileName8 = str(datetime.datetime.now()).replace(" ", "+")
filePath8 = '/home/pi/testImages/' + fileName8 + '.jpg'
camera.capture(filePath8)
print(filePath8)
frame8 = ('image', open(filePath8, 'rb'))
time.sleep(waitTime)






files = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8]

# files = [('frame1', frame1), 
#          ('frame2', frame2), 
#          ('frame3', frame3), 
#          ('frame4', frame4), 
#          ('frame5', frame5), 
#          ('frame6', frame6),
#          ('frame7', frame7),
#          ('frame8', frame8)]

data = [('timestamp1', fileName1),
        ('timestamp2', fileName2),
        ('timestamp3', fileName3),
        ('timestamp4', fileName4),
        ('timestamp5', fileName5),
        ('timestamp6', fileName6),
        ('timestamp7', fileName7),
        ('timestamp8', fileName8)]


print("after da file array")


# files = {'frame1': frame1, 'frame2': frame2, 'frame3': frame3, 'frame4': frame4, 'frame5': frame5, 'frame6': frame6, 'frame7': frame7, 'frame8': frame8}
# data = {'timestamp1': fileName1, 'timestamp2': fileName2, 'timestamp3': fileName3, 'timestamp4': fileName4, 'timestamp5': fileName5, 'timestamp6': fileName6, 'timestamp7': fileName7, 'timestamp8': fileName8}
# requests.post(ec2url1, files=files)
requests.post(ec2url1, files=files, data=data)

print("after da post")


os.remove(filePath1) #cleanup
os.remove(filePath2)
os.remove(filePath3)
os.remove(filePath4)
os.remove(filePath5) 
os.remove(filePath6)
os.remove(filePath7)
os.remove(filePath8)


print("after da remove")


camera.stop_preview()