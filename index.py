from flask import Flask, request, jsonify, session
from flask_cors import CORS
from bcrypt import hashpw, gensalt, checkpw
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set a secret key for sessions (required for session management)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')

# In-memory "database" for demonstration purposes
users = []

# Helper functions for user management
def find_user(username):
    """Find a user by username."""
    return next((user for user in users if user['username'] == username), None)

def add_user(user):
    """Add a new user to the database."""
    users.append(user)

# Routes
@app.route('/')
def home():
    return "Welcome to the User Authentication API"

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if find_user(username):
        return jsonify({"message": "User already exists"}), 400

    # Hash the password before storing it
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    add_user({"username": username, "password": hashed_password})
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = find_user(username)
    if not user or not checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"message": "Invalid credentials"}), 401

    # Store the username in the session to indicate the user is logged in
    session['username'] = username
    return jsonify({"message": "Login successful"})

@app.route('/profile', methods=['GET'])
def profile():
    """Get the profile of the logged-in user."""
    if 'username' not in session:
        return jsonify({"message": "Unauthorized"}), 401

    username = session['username']
    return jsonify({"message": "Profile data", "user": username})

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('username', None)
    return jsonify({"message": "Logout successful"})

# Vercel handler
def handler(event, context):
    """Handler for Vercel serverless functions."""
    # Wrap the Flask app in a WSGI middleware for Vercel compatibility
    wsgi_app = DispatcherMiddleware(app, {
        '/': app
    })

    # Use the WSGI app to handle the event
    response = Response.from_app(wsgi_app, event)
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data().decode('utf-8')
    }

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)