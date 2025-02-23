import requests

BASE_URL = "http://127.0.0.1:5000"

def test_register():
    url = f"{BASE_URL}/register"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    try:
        print("Register:", response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)

def test_login():
    url = f"{BASE_URL}/login"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    try:
        print("Login:", response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)

def test_profile(token):
    url = f"{BASE_URL}/profile"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    try:
        print("Profile:", response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)

# Run the tests
test_register()
test_login()
