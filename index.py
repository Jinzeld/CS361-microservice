from flask import Flask, request, jsonify, session
from flask_cors import CORS
from bcrypt import hashpw, gensalt, checkpw
from utils.db import add_user, find_user
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()  # Loads the environment variables from the .env file

# Configure a secret key for sessions
app.secret_key = os.getenv('SECRET_KEY')  # Secret key loaded from .env

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

    # Store the username in the session to indicate the user is logged in
    session['username'] = username
    return jsonify({"message": "Login successful"})

# Protected Profile Route
@app.route('/profile', methods=['GET'])
def profile():
    # Check if the user is logged in by verifying the session
    if 'username' not in session:
        return jsonify({"message": "Unauthorized"}), 401

    current_user = session['username']
    return jsonify({"message": "Profile data", "user": current_user})

# User Logout
@app.route('/logout', methods=['POST'])
def logout():
    # Remove the username from the session
    session.pop('username', None)
    return jsonify({"message": "Logout successful"})

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the User Authentication API"

# Vercel handler
def handler(event, context):
    return app(event, context)

# This is required for Vercel to recognize the app
if __name__ == '__main__':
    app.run(debug=True)