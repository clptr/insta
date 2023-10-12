from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="views")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

Session(app)
db = SQLAlchemy(app)

from application import routes
from application.models import *