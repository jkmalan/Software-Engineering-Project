from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login = LoginManager()
crypt = Bcrypt()
mail = Mail()

bp = Blueprint('main', __name__, template_folder='templates')

from app.main import routes
