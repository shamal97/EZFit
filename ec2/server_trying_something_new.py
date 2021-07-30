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
    os.system("./build/examples/openpose/openpose.bin --image_dir examples/media/ --write_json output/ --display 0 --render_pose 0")
    return "sup baby"

@app.route('/giveFrame', methods=['POST']) #allow POST requests
def getFrame():

    app.logger.info('/giveFrame been hit')
    app.logger.info(request)
    # app.logger.info(request.headers)
    # app.logger.info('image in files')

    app.logger.info()

    # frameImage1 = request.files['frame1']
    # timestamp1 = request.form['timestamp1']
    # imageFilename1 = timestamp1 + ".jpg"
    # filepath1 = os.path.join(app.root_path, "input", imageFilename1)
    # frameImage1.save(filepath1)
    # app.logger.info('saved image1')
    # app.logger.info(filepath1)

    # frameImage2 = request.files['frame2']
    # timestamp2 = request.form['timestamp2']
    # imageFilename2 = timestamp2 + ".jpg"
    # filepath2 = os.path.join(app.root_path, "input", imageFilename2)
    # frameImage2.save(filepath2)
    # app.logger.info('saved image2')
    # app.logger.info(filepath2)

    # frameImage3 = request.files['frame3']
    # timestamp3 = request.form['timestamp3']
    # imageFilename3 = timestamp3 + ".jpg"
    # filepath3 = os.path.join(app.root_path, "input", imageFilename3)
    # frameImage3.save(filepath3)
    # app.logger.info('saved image3')
    # app.logger.info(filepath3)

    # frameImage4 = request.files['frame4']
    # timestamp4 = request.form['timestamp4']
    # imageFilename4 = timestamp4 + ".jpg"
    # filepath4 = os.path.join(app.root_path, "input", imageFilename4)
    # frameImage4.save(filepath4)
    # app.logger.info('saved image4')
    # app.logger.info(filepath4)





    # frameImage5 = request.files['frame5']
    # timestamp5 = request.form['timestamp5']
    # imageFilename5 = timestamp5 + ".jpg"
    # filepath5 = os.path.join(app.root_path, "input", imageFilename5)
    # frameImage5.save(filepath5)
    # app.logger.info('saved image5')
    # app.logger.info(filepath5)

    # frameImage6 = request.files['frame6']
    # timestamp6 = request.form['timestamp6']
    # imageFilename6 = timestamp6 + ".jpg"
    # filepath6 = os.path.join(app.root_path, "input", imageFilename6)
    # frameImage6.save(filepath6)
    # app.logger.info('saved image6')
    # app.logger.info(filepath2)

    # frameImage7 = request.files['frame7']
    # timestamp7 = request.form['timestamp7']
    # imageFilename7 = timestamp7 + ".jpg"
    # filepath7 = os.path.join(app.root_path, "input", imageFilename7)
    # frameImage7.save(filepath7)
    # app.logger.info('saved image7')
    # app.logger.info(filepath7)

    # frameImage8 = request.files['frame8']
    # timestamp8 = request.form['timestamp8']
    # imageFilename8 = timestamp8 + ".jpg"
    # filepath8 = os.path.join(app.root_path, "input", imageFilename8)
    # frameImage8.save(filepath8)
    # app.logger.info('saved image8')
    # app.logger.info(filepath8)

    # #run and make image output
    # os.system("./build/examples/openpose/openpose.bin --image_dir input/ --write_json output/json --write_images output/images --display 0 --render_pose 1")


    # #run dont make image output
    # # os.system("./build/examples/openpose/openpose.bin --image_dir input/ --write_json output/json --display 0 --render_pose 0")
    # os.system("rm input/" + imageFilename1)
    # os.system("rm input/" + imageFilename2)
    # os.system("rm input/" + imageFilename3)
    # os.system("rm input/" + imageFilename4)
    # os.system("rm input/" + imageFilename5)
    # os.system("rm input/" + imageFilename6)
    # os.system("rm input/" + imageFilename7)
    # os.system("rm input/" + imageFilename8)


    # jsonFilename = "output/json/" + timestamp + "_keypoints.json"
    # renderedImagePath = "output/images/" + timestamp + "_rendered.png"
    # backendUrl = "http://ec2-54-208-31-8.compute-1.amazonaws.com:8080/workout/frame"
    # jsonFile = {'file': open(jsonFilename, 'rb')}
    # renderedImage = {'file': open(renderedImagePath, 'rb')}


    # with open(jsonFilename) as f:
    #     d = json.dumps(json.load(f))
    #     requestToSend = "POST /workout/frame HTTP/1.1 \nConnection: keep-alive \n\n" + str(d) + "\n\n"


    # print("da request: \n \n \n")
    # print(requestToSend)
    # print( "\n \n \n ")

    # nakulSocket.sendall(requestToSend)

    # request = requests.post(backendUrl, files=jsonFile)




    # uploadFile(renderedImagePath, BUCKET_NAME)


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
    # nakulSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # nakulSocket.connect(("ec2-54-208-31-8.compute-1.amazonaws.com", 8080))
    app.run(host='0.0.0.0', debug=True, port=8081)   #this for running on ec2
    # app.run(debug=True, port=8081)   #this for local development