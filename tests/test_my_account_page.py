import allure
from helpers import restore_password_page
from conftest import driver, random_user
from locators.my_account_locators import MyAccountLocators
from pages.my_account_page import MyAccountPage


class TestMyAccountPage:
    @allure.title("Test go to restore password page")
    def test_go_to_restore_password_page(self, driver, random_user):
        page = restore_password_page(driver, random_user)
        assert page.get_restore_password_email_field_text() == "Email"

    @allure.title("Test input data in email field")
    def test_input_data_in_email_field(self, driver, random_user):
        page = restore_password_page(driver, random_user)
        page.input_data_in_restore_password_email_field_and_click()
        assert page.get_remember_password_link_text() == "Войти"

    @allure.title("Test click on show password, make it shine")
    def test_click_on_show_password_make_it_shine(self, driver, random_user):
        page = restore_password_page(driver, random_user)
        page.input_data_in_restore_password_email_field_and_click()
        page.input_data_in_restore_password_form_field_and_click_on_eye()
        new_password_input = page.find_element_and_wait(MyAccountLocators.RESTORE_PASSWORD_NEW_PASSWORD_INPUT_SHOWN)
        assert page.get_attribute_value(new_password_input, "type") == "text"

    @allure.title("Test go to my account profile")
    def test_go_to_my_account_profile(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user["email"], random_user["password"])
        my_account_page.click_on_my_account()
        assert my_account_page.get_my_account_text() == "В этом разделе вы можете изменить свои персональные данные"

    @allure.title("Test go to my account orders history")
    def test_go_to_my_account_orders_history(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user["email"], random_user["password"])
        my_account_page.click_on_my_account()
        my_account_page.click_on_my_orders_feed_button()
        assert my_account_page.get_aria_current_attribute() == "page"

    @allure.title("Test my account logout")
    def test_my_account_logout(self, driver, random_user):
        my_account_page = MyAccountPage(driver)
        my_account_page.create_user_and_login(random_user["email"], random_user["password"])
        my_account_page.click_on_my_account()
        my_account_page.click_on_my_orders_feed_button()
        my_account_page.click_on_my_account_exit_button()
        assert my_account_page.get_enter_button_text() == "Войти"
