from flasker import db
import datetime

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.Unicode(128))
	name = db.Column(db.Unicode(128))
	password = db.Column(db.Unicode(1024))
	authenticated = db.Column(db.Boolean, default=False)
	posts = db.relationship('Post')
	
	#-----login requirements-----
	def is_active(self):
		#all users are active
		return True 

	def get_id(self):
		# returns the user e-mail but who calls it and who verifies this?
		return unicode(self.email)

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		# False as we do not support annonymity
		return False
	
	#constructor
	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password
		self.authenticated = True

	@staticmethod
	def create_user(name, email,password):
		#check e-mail is not occupied
		try: 
			if User.get_user(email):
				# occupied
				print "its occupied"
				return False
			u = User(name,email,password)
			db.session.add(u)
			db.session.commit()
			return True
		except:
			print "couldn't create user"

		return False

	@staticmethod
	def get_user(email):
		# checks for the existence of a unique e-mail in db
		q = User.query.filter_by(email=email)
		count = q.count()
		if count == 1:
			return q.first()
		return None


class Post(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	ts = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	text = db.Column(db.Text)
	
	def __init__(self, user_id, text):
		self.user_id = user_id
		self.text = text


	@staticmethod
	def create_post(input):
		#based on user name get userid
		email = input.get('email')
		text = input.get('Body')

		if email and text:
			u = User.get_user(email)
			if u:
				p = Post(u.id, text)
				db.session.add(p)
				db.session.commit()

# the following line will create the models within MySQL
db.create_all();
print 'db created'
	
