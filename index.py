from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt, checkpw
from utils.db import add_user, find_user
import os

app = Flask(__name__)

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400
    
    if find_user(username):
        return jsonify({"message": "User already exists"}), 400

    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    add_user({"username": username, "password": hashed_password})
    return jsonify({"message": "User registered successfully"}), 201

if __name__ == 'main':
    app.run(debug=True)