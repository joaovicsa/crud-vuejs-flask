from flask import Flask, request, jsonify
from dataclasses import asdict

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([user for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = parse_user(data)
    mongo.db.users.insert_one(asdict(user))
    return jsonify({"msg": "User added successfully"}), 201

@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    data = request.json
    user = parse_user(data)
    mongo.db.users.update_one({"username": username}, {"$set": asdict(user)})
    return jsonify({"msg": "User updated successfully"})

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    mongo.db.users.delete_one({"username": username})
    return jsonify({"msg": "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)