import requests
from selenium import webdriver
import pytest

API_BASE_URL = "http://localhost:5000"
USERS_ENDPOINT = f"{API_BASE_URL}/users"


#Scenario 1: Verify Successful GET Request of a specific user(Efi)    
def test_get_specific_user_data():
    # Exist User ID
    user_id = "Efi"  
    user_data = {
        "name": "Efi",
        "id": "987654"
    }

    # Step 1: Make a GET request to retrieve the specific user's payload
    response = requests.get(f"{USERS_ENDPOINT}/{user_id}")

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200 #Expected result 1

    # Step 2: Extract user data from the API response
    specific_user_data = response.json()

    # Verify the payload returned matches the expected JSON data
    assert response.json() == user_data #Expected result 2

    
#Scenario 2: Verify  GET Request fails in a case user does not exist    
def test_user_not_exist():
    
    nonexist_user_id = "blabla"  
    
    # Step 1: Make a GET request 
    response = requests.get(f"{USERS_ENDPOINT}/{nonexist_user_id}")

    # Assert the response status code is 404 (Not Found)
    assert response.status_code == 404 #Expected result 1
    assert response.json()["message"] == "User ID does not exist" #Expected result 2
    

#Scenario 3: Verify  GET Request fails in a case of invalid input (/use)   
API_BASE_URL = "http://localhost:5000"
USERS_ENDPOINT = f"{API_BASE_URL}/use"



def test_invalid_request_api_and_verify_display():
    # Make an invalid GET request to the users endpoint 
    response = requests.get(USERS_ENDPOINT)

    # Assert the response status code is 400 (Bad Request) 
    assert response.status_code == 400 #Expected result 1
    assert response.json()["message"] == "Bad request " #Expected result 2


#Scenario 4: Get all Users data
API_BASE_URL = "http://localhost:5000"
USERS_ENDPOINT = f"{API_BASE_URL}/users"


def test_get_all_users():
    # Make  GET request to the users endpoint 
    response = requests.get(USERS_ENDPOINT)

    # Assert the response status code is 200 (OK) 
    assert response.status_code == 200 #Expected result 1

# Step 2: Extract user data from the API response
    specific_user_data = response.json()

