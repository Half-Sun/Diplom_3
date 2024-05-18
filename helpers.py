import allure
from locators.my_account_locators import MyAccountLocators
from pages.my_account_page import MyAccountPage

@allure.step("Restore passsword")
def restore_password_page(driver, user_data):
    page = MyAccountPage(driver)
    page.go_to_site()
    page.click_on_my_account()
    page.click_on_restore_password_button()
    return page

@allure.step("Create user and login")
def create_user_and_login(driver, random_user):
    email = random_user["email"]
    password = random_user["password"]
    base_url = "https://stellarburgers.nomoreparties.site"
    driver.get(base_url)
    driver.find_element(*MyAccountLocators.GO_TO_MY_ACCOUNT).click()
    driver.find_element(*MyAccountLocators.RESTORE_PASSWORD_EMAIL_FIELD_INPUT).send_keys(email)
    driver.find_element(*MyAccountLocators.MY_ACCOUNT_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*MyAccountLocators.MY_ACCOUNT_ENTER_BUTTON).click()
