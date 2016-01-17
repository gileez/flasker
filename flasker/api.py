from flasker import app
from flask import request, jsonify
from flasker.models import User
import hashlib

@app.route("/api/login", methods=["POST", "GET"])
def login():
	print "got a login request"
	ret = {'status': 'FAIL'}
	# get user data from client
	email = request.args.get('email')
	# TODO encryption should be on the client
	password = hashlib.md5( request.args.get('password') ).hexdigest()
	u = User.get_user(email)
	if u:
		if u.password == password:
			ret['status'] = 'OK'

	# do the login (save cookie)
	return jsonify(ret)

@app.route("/api/signup", methods=["POST","GET"])
def signup():
	ret = {'status': 'FAIL'}
	name = request.args.get('name')
	email = request.args.get('email')
	# TODO encryption should be on the client
	password = hashlib.md5( request.args.get('password') ).hexdigest()
	if User.create_user(name,email,password):
		ret['status']= 'OK'

	return jsonify(ret)

@app.route("/api/post", methods=["POST","GET"])
def addPost():
	print '==made it to addpost=='
	ret = {'status': 'FAIL'}
	print request.get_json()
	print request.view_args
	body = request.get_json().get('Body')
	print "body is %s" %body
	if body:
		ret['body'] = body
		ret['status'] = 'OK'

	return jsonify(ret)