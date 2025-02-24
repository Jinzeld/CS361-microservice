from flask import Flask, request, jsonify
from flask_cors import CORS
from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from utils.db import add_user, find_user
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()  # Loads the environment variables from the .env file

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # JWT secret key loaded from .env
jwt = JWTManager(app)

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

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = find_user(username)
    if not user or not checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"message": "Login successful", "token": token}) 

# Protected Profile Route
@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({"message": "Profile data", "user": current_user})

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the User Authentication Microservice"

    

if __name__ == 'main':
    app.run(debug=True) 