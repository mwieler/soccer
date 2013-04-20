import os

from flask import Flask # an instance of this class will be the WSGI
    # app
from flask import url_for, render_template

#from flask.ext.sqlalchemy import SQLAlchemy

#from flask_login import LoginManager

soccerapp = Flask(__name__)
soccerapp.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
soccerapp.config['CSRF_ENABLED'] = os.environ['CSRF_ENABLED']
soccerapp.config['SECRET_KEY'] = os.environ['SECRET_KEY']
#db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)

#login_manager = LoginManager()
#login_manager.setup_app(soccerapp)

# @login_manager.user_loader
# def load_user(userid):
#     return User.get(userid)


import soccer.views

#import soccer.forms # necessary?

if __name__ == "__main__": # only run server if script is executed
    # directly from interpreter
    soccerapp.run(debug = True)