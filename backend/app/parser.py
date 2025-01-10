# parser.py
import json
import pymongo 
import time
from dataclasses import asdict
from models import User, UserPreferences

def parse_roles(data):
    roles = []
    if data.get("is_user_admin"):
        roles.append("admin")
    if data.get("is_user_manager"):
        roles.append("manager")
    if data.get("is_user_tester"):
        roles.append("tester")
    return roles


def connect_to_mongodb(uri, database_name):
    client = pymongo.MongoClient(uri)
    db = client[database_name]
    return db

def insert_data_to_mongodb(db, collection_name, data):
    collection = db[collection_name]
    collection.insert_many(data)

if __name__ == "__main__":
    mongodb_uri = "mongodb://localhost:27017/"
    database_name = "users"
    collection_name = "crud"
    file_path = "init.json"

    with open(file_path, 'r') as file:
        data = json.load(file)

    users = []
    for user_data in data["users"]:
        roles = parse_roles(user_data)
        preferences = UserPreferences(timezone=user_data["user_timezone"])
        created_ts = time.mktime(time.strptime(user_data["created_at"], "%Y-%m-%dT%H:%M:%SZ"))

        user = User(
            username=user_data["user"],
            password=user_data["password"],
            roles=roles,
            preferences=preferences,
            active=user_data["is_user_active"],
            created_ts=created_ts
        )

        users.append(asdict(user))


    with open(file_path, 'r') as file:
        raw_data = json.load(file)
    
    
    
    db = connect_to_mongodb(mongodb_uri, database_name)
    insert_data_to_mongodb(db, collection_name, users)
    
    print("Data imported successfully.")

