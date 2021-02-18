from flask import Flask
from datetime import timedelta
from flask_login import LoginManager

from app.routes import *


def create_app():
    app = Flask(__name__)

    return app
