# User Authentication Microservice

## Overview
This microservice provides a user authentication system using Flask, enabling:
- **User Registration:** Allows new users to sign up with a username and password.
- **User Login:** Authenticates existing users and returns a JWT token.
- **Protected Profile Access:** Verifies JWT tokens to grant access to protected resources.

The communication between the client and the microservice is handled through a **REST API** using **HTTP POST** and **GET** requests. JSON Web Tokens (**JWT**) are used for secure authentication.

---

## Communication Contract

### 1. **User Registration**
#### **Endpoint:** `/register`  
**Method:** `POST`  

**Request Body Example:**  
```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

### Example call in python:
```python
import requests

url = "http://localhost:5000/register"
data = {"username": "testuser", "password": "securepassword"}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.json())
```

### Expected response
```json
{
    "message": "User registered successfully"
}
```

### 2. User Login
#### **Endpoint:** `/login`
**Method:** `POST`

**Request Body Example:**
```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

### Example Call in Python:

```python
import requests

url = "http://localhost:5000/login" 
data = {"username": "testuser", "password": "securepassword"}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.json())

# Extracting JWT token from the response
token = response.json().get("token")
print("JWT Token:", token)
```

### Expected Response:
```json
{
    "message": "Login successful",
    "token": "your_jwt_token_here"
}
```

### 3. Access Protected Profile Data
#### **Endpoint:** `/profile`
**Method:** `GET`

#### Headers: Include the JWT token in the Authorization header.
#### Authorization Format: Bearer <JWT_TOKEN>

Example Call in Python:
```python
import requests

url = "http://localhost:5000/profile"
headers = {"Authorization": "Bearer your_jwt_token_here"}
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.json())
```

### Expected Response:
```json
{
    "message": "Profile data",
    "user": "testuser"
}
```

## UML Sequence Diagram
<img src="https://github.com/user-attachments/assets/578fa3be-ecee-46a4-baa7-5950eefd5101" width="500px" height="500px">



## Deployment

```
This microservice is hosted on Vercel. Replace http://localhost:5000 with your deployed Vercel URL when making requests in production.
```

## Additional Notes

```
Environment Variables: Set JWT_SECRET_KEY in a .env file for local development and in Vercel's environment variables for production.

Ensure your teammate writes their own code to make requests, using only the provided communication contract as a reference.
```


