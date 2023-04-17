# importing the packages
from flask import Flask, flash, request, redirect, render_template, url_for
import os
import time
import random
from werkzeug.utils import secure_filename
import shutil
from app import app


# defining the allowed file extensions
ALLOWED_EXTENSIONS = set(['JPG','PNG','JPEG','jpg', 'png', 'jpeg'])
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/form', methods = ['POST'])
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
      flash('No file selected for uploading')
      time.sleep(2)
      return redirect(request.url)
    
    if file and allowed_file(file.filename):
      # saving the name of the file
      filename = secure_filename(file.filename)
      # moving file to upload folder
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      flash('File successfully uploaded')


      # doing analysis and saving the data and charts to the files
      #read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      
      
      # moving the file to processed file after saving the data
      shutil.move(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['PROCESSED_FOLDER'], filename))
      flash('File successfully processed')
      results = os.path.join(app.config['PROCESSED_FOLDER'], filename)
      flash('You can now view the result')

      return render_template('index.html', results=results)
    else:
      flash('That did not work, allowed file types are .jpg, jpeg and .png')
      flash('Please try again')
      return redirect(request.url)

if __name__ == "__main__":
  app.run( # Starts the site
    host='0.0.0.0',  
    port=random.randint(2000, 9000),  
    debug=False
  )