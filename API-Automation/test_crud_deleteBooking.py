import allure
import pytest
import requests


# generate token
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
    booking_id = response.json().get("bookingid")
    print(booking_id)
    return booking_id
@allure.title("Delete a booking")
@allure.description("Verify a booking is deleted successfully")
@pytest.mark.crud
def test_delete_booking():
    booking_id = create_booking()
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    cookie = "token=" + generate_token()
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    #make DELETE request to delete a booking
    responseData = requests.delete(url=url, headers=headers)

    assert responseData.status_code == 201

    # Run get request to Verify that the deleted booking returns 404
    get_response = requests.get(url)
    assert get_response.status_code == 404
