import os
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask_mail import Mail, Message

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'xls','xlsm', 'xltx', 'xltm', 'xml', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
dest_path = 'C:/Users/ankur/Desktop'

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True, MAIL_USERNAME = 'ankurch3006@gmail.com', MAIL_PASSWORD = 'Dipa@0111719'
	)
mail = Mail(app)

def allowed_file(filename):
	return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    if request.method == 'POST':
        for file in request.files.getlist('file'):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_drive = drive.CreateFile({'title':os.path.basename(filename) })
                file_drive.SetContentString(file.read(), filename) 
                file_drive.Upload()
                file.save(os.path.join(dest_path, filename))
                msg = Message("A File Was Uploaded!", sender="ankurch3006@gmail.com", recipients=["ankurch3006@gmail.com"])
                msg.body = f"{filename} was uploaded to {dest_path}"           
                mail.send(msg)
                flash('{} successfully uploaded to {}'.format(filename, dest_path))	
            else:
                flash('file type not allowed')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)