import pdb
import os
from flask import Flask
from flask import render_template, url_for, request, flash, redirect
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
import random

@app.route("/")
def home():
    print "home() called"
    return render_template('main.html') # 'static'
        # is a special argument, defaults to /static

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

def login_required():
    print "login_required called"
    def wrap(restricted_function):
        print "wrap called"
        def decorator():
            print "decorator called"
            if user_exists():
                print "user exists, about to return restricted_function()"
                return restricted_function()
            else:
                print "user does not exist, about to return not_logged_in()"
                return not_logged_in()
        print "about to return decorator function object"
        return decorator
    print "about to return wrap function object"
    return wrap

def user_exists():
    print "user may exist; about to return true or false"
    return random.choice([True,False])
    #return False

def not_logged_in():
    return render_template('denied.html')


@app.route('/secret')
@login_required() # login_required() evaluates to a wrap function object; @ calls wrap
def show_secret():
    print "show_secret called, about to render template"
    return render_template('secret.html')

if __name__ == '__main__':
    print "about to run server"
    app.run(debug=True)