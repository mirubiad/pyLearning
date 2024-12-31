import allure
import pytest
import requests


# generate token
@pytest.fixture()
def generate_token():
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    responseData = requests.post(url=url, json=payload, headers=headers)

    #Store the token in a variable for later use
    token = responseData.json()["token"]
    print(token)
    return token

#Creating a new booking
@pytest.fixture()
def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    payload = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Lunch"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, json=payload, headers=headers)

    assert response.status_code == 200
    booking_id = response.json().get("bookingid") # or we can write response.json().["bookingid"]
    print(booking_id)
    return booking_id