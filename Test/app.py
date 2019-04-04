import os
from flask import Flask, render_template, request
import db
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
  if request.method == "GET":
    return render_template('test.html')
  elif request.method == "POST":
    img_file = request.form['base64']
    db.upload(img_file)
    image = db.search_image(img_file)
    return render_template('image.html', img_file = image)
   

if __name__ == '__main__':
  app.run(debug=True)