import os
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'xls','xlsm', 'xltx', 'xltm', 'xml', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
dest_path = 'C:/Users/ankur/Desktop/Flask_Project'

def allowed_file(filename):
	return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        for file in request.files.getlist('file'):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(dest_path, filename))
                flash('{} successfully uploaded to {}'.format(filename, dest_path))	
            else:
                flash('file type not allowed')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)