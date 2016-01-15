from flasker import app
from flask import request, jsonify
from flasker.models import User

@app.route("/api/login", methods=["POST", "GET"])
def login():
	ret = {'status': 'FAIL'}
	# get user data from client
	email = request.args.get('email')
	password = request.args.get('password')
	#handle it
	if User.check_user(email, password):
		ret['status'] = 'OK'

	# do the login (save cookie)
	return jsonify(ret)

