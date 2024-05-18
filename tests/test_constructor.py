import allure
from conftest import driver
from locators.constructor_locators import ConstructorLocators
from pages.constructor_page import ConstructorPage


class TestConstructor:
    @allure.title("Test going to constructor")
    def test_go_to_constructor(self, driver):
        constructor = ConstructorPage(driver)
        burger_text = constructor.click_on_constructor_button()
        assert burger_text == "Соберите бургер"

    @allure.title("Test clicking on element, pop-up appears")
    def test_click_on_element_pop_up_appears(self, driver):
        constructor = ConstructorPage(driver)
        pop_up = constructor.click_on_constructor_first_element()
        assert pop_up.is_displayed()

    @allure.title("Test clicking on close pop-up, pop-up exits")
    def test_click_on_close_pop_up_exit(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_first_element()
        constructor.click_on_constructor_pop_up_exit_button()
        assert constructor.is_pop_up_closed(ConstructorLocators.INGREDIENT_DETAILS_POP_UP)

    @allure.title("Test adding element to order increases counter")
    def test_add_element_to_order_increase_counter(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_button()
        constructor.add_first_ingredient_to_order()
        assert int(constructor.get_text_from_element(ConstructorLocators.INGREDIENT_COUNTER)) > 0
