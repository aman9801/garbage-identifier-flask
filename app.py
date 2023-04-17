from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'static/processed/'

app = Flask(  
	__name__,
  # Name of html file folder
	template_folder='templates',
  # Name of directory for static files
	static_folder='static'
)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024