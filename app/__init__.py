
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)
CsrfProtect(app)

lm = LoginManager()
lm.init_app(app)

db = SQLAlchemy(app)

from app import views, models