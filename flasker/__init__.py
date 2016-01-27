from flask import Flask, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.login as FL
from flask.ext.superadmin import Admin, model
#from flask.ext.superadmin.contrib import sqlamodel

# define the main app object
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'super secret string'
# create the database object
db = SQLAlchemy(app)

login_manager = FL.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"

'''# Create customized model view class
class MyModelView(sqlamodel.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


# Create customized index view class
class MyAdminIndexView(superadmin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
'''
# import app modules
from models import *
import views
import api

# Create admin
admin = Admin(app)
admin.register(User, session=db.session)
admin.register(Post, session=db.session)

# Add view
#admin.add_view(MyModelView(User, db.session))
#admin.setup_app(app)