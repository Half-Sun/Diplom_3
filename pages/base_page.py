import logging

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    @allure.step("Go to site")
    def go_to_site(self):
        base_url = "https://stellarburgers.nomoreparties.site"
        self.driver.get(base_url)

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Find element and wait")
    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Click on element")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Input data to element")
    def input_data_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    @allure.step("Get text from element")
    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).get_attribute('innerHTML')

    @allure.step("Get attribute value")
    def get_attribute_value(self, locator, attribute_name):
        try:
            return locator.get_attribute(attribute_name)
        except Exception as e:
            self.logger.error(f"An error occurred while getting attribute '{attribute_name}': {e}")
            return None

    @allure.step("Drag and drop")
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_and_wait(source_locator)
        target_element = self.find_element_and_wait(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Wait for element to disappear")
    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step("Wait until text changed")
    def wait_for_text_to_change(self, locator, old_text):
        WebDriverWait(self.driver, 400).until(
            lambda d: d.find_element(*locator).text != old_text,
            f"Text did not change from '{old_text}' within 10 seconds."
        )