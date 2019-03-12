from flask import Flask
from flask import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'enter your mailtrap smtp username'
app.config['MAIL_PASSWORD'] = 'enter your mailtrap smtp password'

mail = Mail(app)
from app import views