import allure
import pytest
import requests


@allure.title("GET Request of RestFUL Booker")
@allure.description("TC#1||verify that GET request with Booking ID gives response")
@allure.testcase("TC#1")
@allure.label(label_type="owner")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/280"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200

@allure.title("GET Request of RestFUL Booker")
@allure.description("TC#2||verify that GET request with  invalid Booking ID gives response 404")
@allure.testcase("TC#2")
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/io"
    responseData = requests.get(url)
    assert responseData.status_code == 404