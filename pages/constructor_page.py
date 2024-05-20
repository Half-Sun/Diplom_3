import allure
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step("Click on constructor button")
    def click_on_constructor_button(self):
        self.go_to_site()
        self.click_on_element(ConstructorLocators.GO_TO_MY_ACCOUNT)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        burger_text = self.get_text_from_element(ConstructorLocators.BURGER_TEXT)
        return burger_text

    @allure.step("Click on first ingredient in constructor")
    def click_on_constructor_first_element(self):
        self.go_to_site()
        self.click_on_element(ConstructorLocators.FIRST_INGREDIENT)
        pop_up = self.find_element_and_wait(ConstructorLocators.INGREDIENT_DETAILS_POP_UP)
        return pop_up

    @allure.step("Click on exit button in ingredient details pop-up")
    def click_on_constructor_pop_up_exit_button(self):
        self.click_on_element(ConstructorLocators.INGREDIENT_DETAILS_POP_UP_CLOSE_BUTTON)

    @allure.step("Check if pop-up is closed")
    def is_pop_up_closed(self, locator):
        return self.wait_for_element_to_disappear(locator)

    @allure.step("Add first ingredient to order")
    def add_first_ingredient_to_order(self):
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)

    @allure.step("Add first ingredient to order and drag and drop")
    def add_click_on_order_button_and_drag_and_drop(self):
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)

