import allure
import pytest
import requests


@allure.title("Create New Booking")
@allure.description("TC#1|| Verify that create booking is working")
@pytest.mark.crud
def test_create_new_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    payload = {
        "firstname": "Tin",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    header = {"Content-Type": "application/json"}
    response_data = requests.post(url=url, json=payload, headers=header)

    # Print the full JSON response for debugging
    print(response_data.json())

    # Validate the response status code
    assert response_data.status_code == 200

    # Store the JSON response in variable for validation
    response = response_data.json()

    # Validate specific fields in the response
    assert response["booking"]["totalprice"] > 0
    assert response["booking"]["firstname"] == "Tin"

    # Check required keys in response
    required_keys = ["firstname", "lastname", "totalprice", "depositpaid"]
    for key in required_keys:
        assert key in response["booking"], f"Key '{key}' is missing"


@allure.title("Create New Booking negative")
@allure.description("TC#2|| Verify that create booking is giving 500 error when empty payload is entered")
@pytest.mark.crud
def test_create_new_booking_emptyPayload():
    url = "https://restful-booker.herokuapp.com/booking"
    payload = {}
    header = {"Content-Type": "application/json"}
    response_data = requests.post(url=url, json=payload, headers=header)
    assert response_data.status_code == 500


print("test passed")




