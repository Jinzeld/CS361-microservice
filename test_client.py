import requests

BASE_URL = "https://cs-361-microservice-a.vercel.app"

def test_register():
    url = f"{BASE_URL}/register"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    print("Register Status Code:", response.status_code)
    print("Register Response Text:", response.text)

def test_login():
    url = f"{BASE_URL}/login"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    print("Login Status Code:", response.status_code)
    print("Login Response Text:", response.text)

    try:
        data = response.json()
        token = data.get("token")
        if token:
            print("Login Token:", token)
            test_profile(token)
        else:
            print("No token received!")
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)

def test_profile(token):
    url = f"{BASE_URL}/profile"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    print("Profile Status Code:", response.status_code)
    print("Profile Response Text:", response.text)

# Run the tests
test_register()
test_login()
