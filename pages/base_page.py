from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from conftest import random_user
import allure
from locators.constructor_locators import ConstructorLocators
from locators.my_account_locators import MyAccountLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def execute(self, driver_command, params=None):
        return self.driver.execute(driver_command, params)

    @allure.step("Go to site")
    def go_to_site(self):
        base_url = "https://stellarburgers.nomoreparties.site"
        self.driver.get(base_url)

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 100).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Find element and wait")
    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Find element and wait")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 100).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step("Find element and wait")
    def wait_for_text_to_change(self, locator, old_text):
        WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element(*locator).text != old_text,
            f"Text did not change from '{old_text}' within 10 seconds."
        )
    @allure.step("Input data to element")
    def input_data_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    @allure.step("Input data to element")
    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).get_attribute('innerHTML')

    @allure.step("Input data to element")
    def get_attribute_value(self, locator, attribute_name):
        try:
            return locator.get_attribute(attribute_name)
        except Exception as e:
            print(f"An error occurred while getting attribute '{attribute_name}': {e}")
            return None

    @allure.step("Perform drag&drop")
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_and_wait(source_locator)
        target_element = self.find_element_and_wait(target_locator)
        actions = ActionChains(self)
        actions.drag_and_drop(source_element, target_element).perform()


