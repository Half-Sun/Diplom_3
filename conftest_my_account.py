import pytest
from pages.my_account_page import MyAccountPage
from conftest import driver

@pytest.fixture
def restore_password_page(driver, random_user):
    user_data = random_user
    page = MyAccountPage(driver)
    page.go_to_site()
    page.click_on_my_account()
    page.click_on_restore_password_button()
    return page
