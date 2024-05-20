import allure
import pytest
from selenium import webdriver
import requests
from faker import Faker

from locators.my_account_locators import MyAccountLocators
from pages.my_account_page import MyAccountPage

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
    access_token = response.json()["accessToken"]

    yield {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token
    }

    delete_user_url = "https://stellarburgers.nomoreparties.site/api/auth/user"
    headers = {"Authorization": f"{access_token}"}
    requests.delete(delete_user_url, headers=headers)

@pytest.fixture
def restore_password_page(random_user, driver):
    page = MyAccountPage(driver)
    page.go_to_site()
    page.click_on_my_account()
    page.click_on_restore_password_button()
    return page

@pytest.fixture(scope="function")
def create_user_and_login(driver, random_user):
    page = MyAccountPage(driver)
    email = random_user["email"]
    password = random_user["password"]
    page.go_to_site()
    page.click_on_my_account()
    page.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT, email)
    page.input_data_to_element(MyAccountLocators.MY_ACCOUNT_PASSWORD_FIELD, password)
    page.click_on_element(MyAccountLocators.MY_ACCOUNT_ENTER_BUTTON)
    return page