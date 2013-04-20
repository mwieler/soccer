import os
from flask import Flask
from flask import render_template, url_for, request, flash, redirect
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

@app.route("/")
def home():
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

if __name__ == '__main__':
    app.run(debug=True)