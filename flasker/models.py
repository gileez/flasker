from flasker import db
import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128))
	email = db.Column(db.Unicode(128))
	password = db.Column(db.Unicode(1024))
	posts = db.relationship('Post')

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

	@staticmethod
	def create_user(name, email,password):
		try:
			#check e-mail is not occupied
			if User.get_user(email):
				# occupied
				print "its occupied"
				return False
			u = User(name,email,password)
			db.session.add(u)
			db.session.commit()
			return True
		except:
			pass

		return False

	@staticmethod
	def get_user(email):
		# checks for the existence of a unique e-mail in db
		q = User.query.filter_by(email=email)
		count = q.count()
		if count == 1:
			return q.first()
		elif count > 1:
			print "internal error. multiple occurences of user %s" %email
			return False
		return False




class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	ts = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	text = db.Column(db.Text)

# the following line will create the models within MySQL
db.create_all();
print 'db created'
	
