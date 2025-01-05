import allure
import pytest
import requests


#verify that booking is deleted by get request with the deleted booking id
@allure.title("Verify deleted booking is not found")
@allure.description("Check that a deleted booking cannot be accessed")
def test_deleted_booking_notfound(generate_token,create_booking):#using fixtures
    #create bookingID
    booking_id = create_booking
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    cookie = "token=" + generate_token
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    # make DELETE request to delete a booking
    responseData = requests.delete(url=url, headers=headers)

    # Run get request to Verify that the deleted booking returns 404
    get_response = requests.get(url)
    assert get_response.status_code == 404