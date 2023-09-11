from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

# Create the Flask application
app = Flask(__name__)

# loading environment variables
load_dotenv()

# retrieving environment variables from .env file
DB_TYPE = os.getenv("DB_TYPE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    DB_TYPE + DB_USER + DB_PASSWORD + DB_HOST + DB_NAME
)

# Configure the Flask app with a SQLite database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# form security
SECRET_KEY = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = SECRET_KEY

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

# encryption stuff
bcrypt = Bcrypt(app)

# login stuff
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Import your routes and models
from application.routes import routes
