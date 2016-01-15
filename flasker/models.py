from flasker import db
import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128))
	email = db.Column(db.Unicode(128))
	password = db.Column(db.Unicode(1024))
	posts = db.relationship('Post')

	@staticmethod
	def create_user(name, email,password):
		try:
			#check e-mail is not occupied
			u = User()
	 		u.name = name
			u.email = email
			u.password = password
			db.session.add(u)
			db.session.commit()
			return True
		except:
			pass

		return False

	@staticmethod
	def check_user(email, password):
		u = User.query.filter_by(email=email, password=password).first()
		if u:
			return True
		return False


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	ts = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	text = db.Column(db.Text)

# the following line will create the models within MySQL
db.create_all();
print 'db created'
	
