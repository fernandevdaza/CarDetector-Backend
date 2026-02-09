import requests
import sys

BASE_URL = "http://localhost:8001"

def verify_token():
    # 1. Create a user
    email = "test_token@example.com"
    password = "password123"
    first_name = "Token"
    last_name = "User"
    user_data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "role": "user"
    }
    
    print(f"Creating user {email}...")
    response = requests.post(f"{BASE_URL}/auth/", json=user_data)
    if response.status_code == 201:
        print("User created successfully.")
    elif response.status_code == 500: # User might already exist
        print("User might already exist, trying to login...")
    else:
        print(f"Failed to create user: {response.status_code} {response.text}")

    # 2. Login to get token
    print("Logging in...")
    login_data = {
        "username": email,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/auth/token", data=login_data)
    if response.status_code != 200:
        print(f"Login failed: {response.status_code} {response.text}")
        return
    
    token_data = response.json()
    print("Login successful.")
    
    # 3. Verify token response fields
    print("Verifying token response fields...")
    expected_fields = ["access_token", "token_type", "user_id", "role", "email", "first_name", "last_name"]
    missing_fields = [field for field in expected_fields if field not in token_data]
    
    if missing_fields:
        print(f"Verification FAILED. Missing fields: {missing_fields}")
        return

    if token_data["email"] != email:
        print(f"Verification FAILED. Email mismatch: expected {email}, got {token_data['email']}")
        return
        
    if token_data["first_name"] != first_name:
        print(f"Verification FAILED. First name mismatch: expected {first_name}, got {token_data['first_name']}")
        return

    if token_data["last_name"] != last_name:
        print(f"Verification FAILED. Last name mismatch: expected {last_name}, got {token_data['last_name']}")
        return

    print("Verification complete! All fields present and correct.")

if __name__ == "__main__":
    try:
        verify_token()
    except Exception as e:
        print(f"An error occurred: {e}")
