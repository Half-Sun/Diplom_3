from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def execute(self, driver_command, params=None):
        return self.driver.execute(driver_command, params)

    def click_on_constructor_button(self):
        self.go_to_site()
        self.click_on_element(ConstructorLocators.GO_TO_MY_ACCOUNT)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        burger_text = self.get_text_from_element(ConstructorLocators.BURGER_TEXT)
        return burger_text

    def click_on_constructor_first_element(self):
        self.go_to_site()
        self.click_on_element(ConstructorLocators.FIRST_INGREDIENT)
        pop_up = self.find_element_and_wait(ConstructorLocators.INGREDIENT_DETAILS_POP_UP)
        return pop_up

    def click_on_constructor_pop_up_exit_button(self):
        self.click_on_element(ConstructorLocators.INGREDIENT_DETAILS_POP_UP_CLOSE_BUTTON)

    def is_pop_up_closed(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return True

    def add_first_ingredient_to_order(self):
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
