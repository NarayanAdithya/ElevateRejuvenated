from flask import Flask,request,redirect,url_for
from flask.templating import render_template
import os
app=Flask(__name__,static_folder='Landing-Page-master/assets/',template_folder='Landing-Page-master/')
print(app.template_folder)
print(os.getcwd())

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)