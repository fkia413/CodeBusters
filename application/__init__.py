from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

# Create the Flask application
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the Flask app with a SQLite database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#    basedir, "database.db"
# )

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # Disable tracking modifications (optional)
app.config["SECRET_KEY"] = "sdasdadkqwepqhed9889oifd"  # Replace with a secret key

# Create the SQLAlchemy database object
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import your routes and models
from application.routes import routes

from application.modules import models
