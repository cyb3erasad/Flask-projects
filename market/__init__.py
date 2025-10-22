from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'e68ec732dc5712c12bf80b8e'
db = SQLAlchemy(app)

from market import routes, models

