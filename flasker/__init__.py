from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# define the main app object
app = Flask(__name__)
app.config.from_object('config')

# create the database object
db = SQLAlchemy(app)

# main view 
@app.route('/')
def home():
 	return render_template('index.html')

# import app modules
import flasker.models

# import api
import flasker.api