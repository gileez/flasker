from flasker.app import db
import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128))
	email = db.Column(db.Unicode(128))
	password = db.Column(db.Unicode(1024))

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ts = db.Column(db.DateTime, default=daytime.daytime.utcnow())
	user = db.relationship(User)
	text = db.Column(db.Text)


# the following line will create the models within MySQL
# db.create_all();
	
