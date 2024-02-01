import requests
from selenium import webdriver
import pytest

API_BASE_URL = "http://localhost:5000"
USERS_ENDPOINT = f"{API_BASE_URL}/users"

@pytest.fixture

#Scenario 1: Create a new User
def Create_user_Efi():
    # Step 1:  Define user data
    user_data = {
        "name": "Efi",
        "id": "987654"
    }

    # Step 2: Make a POST request to create a user
    response = requests.post(USERS_ENDPOINT, json=user_data)

    # Assert the response status code is 201 (Created)
    assert response.status_code == 201 #Expected result 1

    # Verify the payload returned matches the expected JSON data
    assert response.json() == user_data #Expected result 2

    # I would add also add a DB data validation: Verify that "Efi" user was added to 'Users' table// #Expected result 3

    
#Scenario 2: Create duplicate User
def Create_duplicate_user():
    # Step 1:  Define user data
    user_data = {
        "name": "Efi",
        "id": "987654"
    }

    # Step 2: Make a POST request to create a user
    response = requests.post(USERS_ENDPOINT, json=user_data)

    # Assert the response status code is 409 (Conflict)
    assert response.status_code == 409 #Expected result 1
    assert response.json()["message"] == "Name already exists" #Expected result 2

    # I would add also add a DB data validation: Verify that "Efi" user was added to 'Users' table only once // #Expected result 3


#Scenario 3: Try to create user with invalid data(empty strings)
def Create_invalid_user_data():
    # Step 1:  Define user data
    invalid_user_data = {
        "name": "",
        "id": ""
    }

    # Step 2: Make a POST request to create a user
    response = requests.post(USERS_ENDPOINT, json=invalid_user_data)

    # Assert the response status code is 400 (Invalid)
    assert response.status_code == 400 #Expected result 1
    assert response.json()["message"] == "You entered an invalid user or ID data" #Expected result 2

    # I would add also add a DB data validation: Verify that "" user was added to 'Users' table  // #Expected result 3



