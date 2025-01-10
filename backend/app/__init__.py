import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = MONGO_URI

    CORS(app)
    mongo.init_app(app)

    # Test the database connection
    with app.app_context():
        try:
            mongo.db.command('ping')
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    from .routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app