import requests

BASE_URL = "https://your-vercel-deployment-url"

def test_register():
    response = requests.post(f"{BASE_URL}/register", json={
        "username": "testUser",
        "password": "password123"
    })
    print("Register:", response.json())

def test_login():
    response = requests.post(f"{BASE_URL}/login", json={
        "username": "testUser",
        "password": "password123"
    })
    data = response.json()
    print("Login:", data)
    
    if "token" in data:
        token = data["token"]
        profile_response = requests.get(f"{BASE_URL}/profile", headers={
            "Authorization": f"Bearer {token}"
        })
        print("Profile:", profile_response.json())

if __name__ == "__main__":
    test_register()
    test_login()
