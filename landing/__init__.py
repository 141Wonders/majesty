import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
csrf = CSRFProtect(app)

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
	SECRET_KEY='1930ef0d3c-6f49-4b35-bc55-4a0522d5719a86',
	WTF_CSRF_SECRET_KEY='1979d85bad-2f08-4d06-8835-1c5e384cb6f286',
	SQLALCHEMY_DATABASE_URI=db_uri,
	SQLALCHEMY_TRACK_MODIFICATIONS=True,
	
	))

db = SQLAlchemy(app)

from .views import *
from .contact.views import *