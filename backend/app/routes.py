import time
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from .models import User, UserPreferences, mongo
from .parser import parse_roles

api = Blueprint('api', __name__)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["users"]
collection = db["crud"]

def parse_user(data):
    roles = parse_roles(data)
    preferences = UserPreferences(timezone=data["user_timezone"])
    created_ts = data.get("created_ts", time.time())
    
    user = User(
        username=data["username"],
        password=data["password"],
        roles=roles,
        preferences=preferences,
        active=data.get("is_user_active", True),
        created_ts=created_ts
    )
    return user

@api.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {'_id': 0}))
    return jsonify(users)

@api.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = parse_user(data)
    collection.insert_one(asdict(user))
    return jsonify({"msg": "User added successfully"}), 201

@api.route('/users/<username>', methods=['PUT'])
def update_user(username):
    data = request.json
    user = parse_user(data)
    collection.update_one({"username": username}, {"$set": asdict(user)})
    return jsonify({"msg": "User updated successfully"})

@api.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    collection.delete_one({"username": username})
    return jsonify({"msg": "User deleted successfully"})

@api.route('/health', methods=['GET'])
def health_check():
    try:
        mongo.db.command('ping')
        return jsonify(status="success", message="Connected to MongoDB"), 200
    except Exception as e:
        return jsonify(status="error", message=f"Failed to connect to MongoDB: {e}"), 500