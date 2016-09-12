
from flask_wtf import Form
from wtforms import PasswordField, TextField, BooleanField, validators


class LoginForm(Form):
    username = TextField('username', [validators.Required()])
    password = PasswordField('password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)
