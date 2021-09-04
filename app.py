from flask import Flask,request,redirect,url_for,Response
from flask.templating import render_template
import os
from camera import VideoCamera
app=Flask(__name__,static_folder='Landing-Page-master/assets/',template_folder='Landing-Page-master/')
print(app.template_folder)
print(os.getcwd())

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/session')
def session():
    return render_template('session.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)