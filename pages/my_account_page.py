from locators.my_account_locators import MyAccountLocators
from pages.base_page import BasePage


class MyAccountPage(BasePage):

    def click_on_my_account(self):
        self.click_on_element(MyAccountLocators.GO_TO_MY_ACCOUNT)

    def click_on_restore_password_button(self):
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_BUTTON)

    def input_data_in_restore_password_email_field_and_click(self):
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT, "Some email")
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_RESTORE_BUTTON)

    def input_data_in_restore_password_form_field_and_click_on_eye(self):
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_NEW_PASSWORD_INPUT, "Some email")
        self.click_on_element(MyAccountLocators.RESTORE_PASSWORD_SHOW_PASSWORD_BUTTON)

    def create_user_and_login(self, email, password):
        self.go_to_site()
        self.click_on_my_account()
        self.input_data_to_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT, email)
        self.input_data_to_element(MyAccountLocators.MY_ACCOUNT_PASSWORD_FIELD, password)
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_ENTER_BUTTON)

    def click_on_my_orders_feed_button(self):
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_ORDERS_HISTORY)

    def click_on_my_account_exit_button(self):
        self.click_on_element(MyAccountLocators.MY_ACCOUNT_EXIT_BUTTON)

    def get_restore_password_email_field_text(self):
        return self.get_text_from_element(MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD)

    def get_remember_password_link_text(self):
        return self.get_text_from_element(MyAccountLocators.RESTORE_PASSWORD_REMEMBER_PASSWORD_LINK)

    def get_my_account_text(self):
        return self.get_text_from_element(MyAccountLocators.MY_ACCOUNT_TEXT)

    def get_aria_current_attribute(self):
        element = self.find_element_and_wait(MyAccountLocators.MY_ACCOUNT_ORDERS_HISTORY)
        return self.get_attribute_value(element, "aria-current")

    def get_enter_button_text(self):
        return self.get_text_from_element(MyAccountLocators.MY_ACCOUNT_ENTER_BUTTON)
