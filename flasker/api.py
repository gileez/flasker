import traceback
from flasker import app, FL, login_manager
from flask import request, jsonify, url_for, redirect, render_template
from flasker.models import User, Post
import flasker.views
import hashlib


@app.route("/api/login", methods=["POST", "GET"])
def login():
	print "got a login request"
	ret = {'status': 'FAIL'}
	# get user data
	isPost = request.method == 'POST'
	if isPost:
		# POST
		email = request.form.get('email')
		password = hashlib.md5( request.form.get('password') ).hexdigest()
	else:
		# GET
		email = request.params.get('email')
		password = hashlib.md5( request.params.get('password') ).hexdigest()	
	u = User.get_user(email)
	if u:
		if u.password == password:
			print "password match"
			ret['status'] = 'OK'
			FL.login_user(u)
			FL.flash("logged in")
			if isPost:
				print "trying to redirect"
				return redirect('/posts')
			else:
				return jsonify(ret)
		else:
			FL.flash("failed authentication")
	# do the login (save cookie)
	return jsonify(ret)

@login_manager.user_loader
def load_user(email):
	return User.get_user(email)

@app.route("/api/signup", methods=["POST","GET"])
def signup():
	ret = {'status': 'FAIL'}
	name = request.form.get('name')
	email = request.form.get('email')
	# TODO encryption should be on the client
	password = hashlib.md5( request.form.get('password') ).hexdigest()
	if User.create_user(name,email,password):
		ret['status']= 'OK'

	return jsonify(ret)

@app.route("/api/logout", methods=["POST","GET"])
@FL.login_required
def logout():
	print "got a logout request"
	FL.logout_user()
	return redirect(url_for('home'))

@app.route("/api/post", methods=["POST","GET"])
@FL.login_required
def addPost():
	print '==made it to addpost=='
	ret = {'status': 'FAIL'}
	Post.create_post(request.get_json())
	body = request.get_json().get('Body')
	print "body is %s" %body
	if body:
		ret['body'] = body
		ret['status'] = 'OK'

	return jsonify(ret)