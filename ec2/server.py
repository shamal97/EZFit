from flask import Flask, request
import os
import requests
import boto
import json
import socket
from boto.s3.key import Key

HOST = "http://ec2-54-208-31-8.compute-1.amazonaws.com/workout/frame"
PORT =  8080

app = Flask(__name__) #create the Flask app

BUCKET_NAME = 'openpose-images'


@app.route('/healthCheck', methods=['GET'])
def healthCheck():
    return 200

@app.route('/giveFrame', methods=['POST']) #allow POST requests
def getFrame():


    app.logger.info('/giveFrame been hit')
    app.logger.info(request)
    # app.logger.info(request.headers)
    # app.logger.info('image in files')

    frameImage = request.files['image']
    app.logger.info('got image')

    timestamp = request.form['timestamp']

    app.logger.info('got file and form')

    imageFilename = timestamp + ".jpg"
    filepath = os.path.join(app.root_path, "input", imageFilename)
    frameImage.save(filepath)
    app.logger.info('saved image')
    app.logger.info(filepath)

    #run and make image output
    os.system("./build/examples/openpose/openpose.bin --image_dir input/ --write_json output/json --write_images output/images --display 0 --render_pose 1")


    #run dont make image output
    # os.system("./build/examples/openpose/openpose.bin --image_dir input/ --write_json output/json --display 0 --render_pose 0")
    os.system("rm input/" + imageFilename)

    jsonFilename = "output/json/" + timestamp + "_keypoints.json"
    renderedImagePath = "output/images/" + timestamp + "_rendered.png"
    # backendUrl = "http://ec2-54-208-31-8.compute-1.amazonaws.com:8080/workout/frame"
    jsonFile = {'file': open(jsonFilename, 'rb')}
    renderedImage = {'file': open(renderedImagePath, 'rb')}


    with open(jsonFilename) as f:
        d = json.dumps(json.load(f))
        requestToSend = "POST /workout/frame HTTP/1.1 \nConnection: keep-alive \n\n" + str(d) + "\n\n"


    print("da request: \n \n \n")
    print(requestToSend)
    print( "\n \n \n ")

    nakulSocket.sendall(requestToSend)

    # request = requests.post(backendUrl, files=jsonFile)




    uploadFile(renderedImagePath, BUCKET_NAME)


    # os.system("rm output/json/" + timestamp) got to remove more than this in output nibba



    return 'hello there'    

def uploadFile(filePath, bucket):
    conn = boto.connect_s3('AKIA5UULSDNNNLY7SOMA', 'ki7Wkhrvr/NlpL3oRXtFRZg0Nscx73sG7CnFZCv7')
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = 'testImage.png'
    k.set_contents_from_filename(filePath)
    # cloudfile.set_contents_from_string(base64.b64decode(cover_art))
    #cloudfile.set_contents_from_string(base64.b64decode(cover_art))
    k.set_metadata('Content-Type', 'image/jpeg') # from https://stackoverflow.com/a/22730676 and https://stackoverflow.com/questions/16156062/using-amazon-s3-boto-library-how-can-i-get-the-url-of-a-saved-key
    k.set_acl('public-read')

    # check this out https://stackoverflow.com/questions/22730051/how-to-upload-a-base64-encoded-string-to-s3-and-access-the-url-in-html-file-in-p



if __name__ == '__main__':
    nakulSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nakulSocket.connect(("ec2-54-208-31-8.compute-1.amazonaws.com", 8080))
    app.run(host='0.0.0.0', debug=True, port=8081)   #this for running on ec2
    # app.run(debug=True, port=8081)   #this for local development