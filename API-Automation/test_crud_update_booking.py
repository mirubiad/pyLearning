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


# update the booking
@allure.title("Upate a Booking")
@allure.description("TC#3|| Verify that booking is successfully updated")
@pytest.mark.crud
def test_update_booking():
    url = "https://restful-booker.herokuapp.com/booking/669"
    payload = {
        "firstname": "Joey",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    cookie = "token=" + generate_token() #calling generate_token function
    header = {"Content-Type": "application/json", "Cookie": cookie}

    # Make the PUT request to update the booking
    response_data = requests.put(url=url, json=payload, headers=header)

    # Validate the response status code
    assert response_data.status_code == 200

    # Print the full JSON response for debugging
    print(response_data.json())

    # Store the JSON response in variable for validation
    response = response_data.json()

    # validate the field are updated
    assert response["firstname"] == "Joey"
    assert response["lastname"] == "Brown"
