import pytest
from selenium import webdriver
import requests
from faker import Faker

fake = Faker()

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver_instance = webdriver.Firefox()
    elif request.param == 'chrome':
        driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

fake = Faker()

@pytest.fixture(scope="function")
def random_user():
    email = fake.email()
    password = fake.password()
    name = fake.name()

    register_url = "https://stellarburgers.nomoreparties.site/api/auth/register"
    register_data = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(register_url, json=register_data)

    if response.status_code != 200:
        raise AssertionError(f"Failed to register user. Response: {response.json()}")

    access_token = response.json()["accessToken"]

    user_info_url = "https://stellarburgers.nomoreparties.site/api/auth/user"
    headers = {"Authorization": f"{access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)

    if user_info_response.status_code != 200:
        raise AssertionError(f"Failed to get user info. Response: {user_info_response.json()}")

    yield {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token
    }

    delete_user_url = "https://stellarburgers.nomoreparties.site/api/auth/user"
    headers = {"Authorization": f"{access_token}"}
    delete_user_response = requests.delete(delete_user_url, headers=headers)

    if not delete_user_response.json().get('success', False):
        print(f"Failed to delete user. Response: {delete_user_response.json()}")