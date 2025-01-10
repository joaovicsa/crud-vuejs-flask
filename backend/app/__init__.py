# __init__.py
import os
from flask import Flask
from flask_cors import CORS
from .models import init_app
from .routes import api

MONGO_URI = os.getenv("MONGO_URI")

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = MONGO_URI

    CORS(app)

    init_app(app)

    app.register_blueprint(api, url_prefix="/api")

    return app