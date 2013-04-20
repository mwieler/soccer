from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required

class LoginForm(Form):
    email = TextField('email', validators = [Required()])
    contact_allowed = BooleanField('remember_me', default = False)