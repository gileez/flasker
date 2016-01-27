from flasker import app, db
from flasker.models import Post, User
from flask import render_template
from flasker import FL

# main view 
@app.route('/')
def home():
 	return render_template('index.html')

@app.route('/posts')
@FL.login_required
def posts():
	#posts = Post.query.join(User).Join(Post)

	posts = []
	_posts = Post.query.all()
	for p in _posts:

		
		#u = User.query.filter_by(id=p.user_id).first()
		if not u:
			continue

		posts.append({
			'user_name': u.name,
			'text': p.text
			})

	return render_template('posts.html', posts=posts)
