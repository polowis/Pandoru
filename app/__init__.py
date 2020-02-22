from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

from app import route
from app import http
from app import config
from app import model

app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
from app.model import user