from flask import render_template
from forms import LoginForm

@soccerapp.route("/")
def home():
    return render_template('main.html') # 'static'
        # is a special argument, defaults to /static

@soccerapp.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user
        flash('Login requested for ID'+form.email+""
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form,title="Login!")

@soccerapp.route("/profile")
def show_profile():
    user = {'name': 'Sean'}
    team = {'name': 'The Friends'}
    players = [{
                'name': 'Matt',
                'email': 'mwieler@optonline.net'
        },
        {
                'name': 'Ben',
                'email': 'brw@email.com'
        },
    ]
    return render_template("profile.html",
        title = 'Your Profile',
        user = user,
        team = team,
        players = players)