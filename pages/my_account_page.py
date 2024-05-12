import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.my_account_locators import MyAccountLocators
from pages.base_page import BasePage
from conftest import driver, random_user


class MyAccountPage(BasePage):
    @allure.step("Click on My Account button")
    def click_on_my_account(self):
        self.click_on_element(MyAccountLocators.GO_TO_MY_ACCOUNT)

    @allure.step("Click on Restore Password button")
    def click_on_restore_password_button(self):
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Input data in Restore Password email field and click")
    def input_data_in_restore_password_email_field_and_click(self):
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT, "Some email")
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_RESTORE_BUTTON)

    @allure.step("Input data in Restore Password form field and click on eye")
    def input_data_in_restore_password_form_field_and_click_on_eye(self):
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_NEW_PASSWORD_INPUT, "Some email")
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_SHOW_PASSWORD_BUTTON)

    @allure.step("Create user and login")
    def create_user_and_login(self, random_user):
        email = random_user["email"]
        password = random_user["password"]
        self.go_to_site()
        self.click_on_my_account()
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT, email)
        self.input_data_to_element(MyAccountLocators.MY_ACCOUNT_PASSWORD_FIELD, password)
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_ENTER_BUTTON)

    @allure.step("Click on My Orders Feed button")
    def click_on_my_orders_feed_button(self):
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_ORDERS_HISTORY)

    @allure.step("Click on My Account exit button")
    def click_on_my_account_exit_button(self):
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_EXIT_BUTTON)