import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators.constructor_locators import ConstructorLocators
from pages.constructor_page import ConstructorPage


class TestConstructor:
    @allure.title("Test go to constructor")
    def test_go_to_constructor(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_button()
        burger_text = constructor.click_on_constructor_button()
        assert burger_text == "Соберите бургер"

    @allure.title("Test click on element, pop-up appears")
    def test_click_on_element_pop_up_appears(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_first_element()
        pop_up = constructor.click_on_constructor_first_element()
        assert pop_up.is_displayed()

    @allure.title("Test click on close pop-up, exit")
    def test_click_on_close_pop_up_exit(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_first_element()
        constructor.click_on_constructor_pop_up_exit_button()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located(
            ConstructorLocators.INGREDIENT_DETAILS_POP_UP))

    @allure.title("Test add element to order, increase counter")
    def test_add_element_to_order_increase_counter(self, driver):
        constructor = ConstructorPage(driver)
        constructor.click_on_constructor_button()
        constructor.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
        assert int(constructor.get_text_from_element(ConstructorLocators.INGREDIENT_COUNTER)) > 0
