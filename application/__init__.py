from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

# Create the Flask application
app = Flask(__name__)

# loading environment variables
load_dotenv()

# Configure the Flask app with a SQLite database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# form security
SECRET_KEY = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = SECRET_KEY

# Create the SQLAlchemy database object
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import your routes and models
from application.routes import routes
