import allure

from conftest import random_user

from conftest import driver
from conftest_my_account import restore_password_page
from locators.my_account_locators import MyAccountLocators
from pages.my_account_page import MyAccountPage


class TestMyAccountPage:
    @allure.title("Test go to restore password page")
    def test_go_to_restore_password_page(self, restore_password_page, random_user):
        assert restore_password_page.get_text_from_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD) == "Email"

    @allure.title("Test input data in email field")
    def test_input_data_in_email_field(self, restore_password_page, random_user):
        restore_password_page.input_data_in_restore_password_email_field_and_click()
        assert restore_password_page.get_text_from_element(MyAccountLocators.RESTORE_PASSWORD_REMEMBER_PASSWORD_LINK) == "Войти"

    @allure.title("Test click on show password, make it shine")
    def test_click_on_show_password_make_it_shine(self, restore_password_page, random_user):
        restore_password_page.input_data_in_restore_password_email_field_and_click()
        restore_password_page.input_data_in_restore_password_form_field_and_click_on_eye()
        new_password_input = restore_password_page.find_element_and_wait(MyAccountLocators.RESTORE_PASSWORD_NEW_PASSWORD_INPUT_SHOWN)
        assert restore_password_page.get_attribute_value(new_password_input, "type") == "text"

    @allure.title("Test go to my account profile")
    def test_go_to_my_account_profile(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user)
        my_account_page.click_on_my_account()
        assert my_account_page.get_text_from_element(MyAccountLocators.MY_ACCOUNT_TEXT) == "В этом разделе вы можете изменить свои персональные данные"

    @allure.title("Test go to my account orders history")
    def test_go_to_my_account_orders_history(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user)
        my_account_page.click_on_my_account()
        my_account_page.click_on_my_orders_feed_button()
        element = my_account_page.find_element_and_wait(MyAccountLocators.MY_ACCOUNT_ORDERS_HISTORY)
        assert my_account_page.get_attribute_value(element, "aria-current") == "page"

    @allure.title("Test my account logout")
    def test_my_account_logout(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user)
        my_account_page.click_on_my_account()
        my_account_page.click_on_my_orders_feed_button()
        my_account_page.click_on_my_account_exit_button()
        assert my_account_page.get_text_from_element(
            MyAccountLocators. MY_ACCOUNT_ENTER_BUTTON) == "Войти"
