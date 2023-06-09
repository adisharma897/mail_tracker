from fileinput import filename
from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['postgres_url']

# initialize the app with the extension
db.init_app(app)


FILENAME = 'job.png'


class MailLogging(db.Model):
    email_id = db.Column(db.Integer, primary_key=True)

    
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/aditya/<int:id>")
def log_tracking(id):
    activity = MailLogging(email_id=id)
    db.session.add(activity)
    db.session.commit()

    return send_file(FILENAME, mimetype='image/png')
