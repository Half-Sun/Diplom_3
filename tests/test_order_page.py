import allure

from conftest import create_user_and_login, driver, random_user
from locators.order_page_locators import OrderPageLocators
from pages.constructor_page import ConstructorPage
from pages.my_account_page import MyAccountPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Test go to order feed")
    def test_go_to_order_feed(self, driver):
        order_page = OrderPage(driver)
        feed_text = order_page.click_on_order_feed()
        assert feed_text == "Лента заказов"

    @allure.title("Test open order to get details")
    def test_open_order_to_get_details(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order_to_open()
        order_pop_up = order_page.find_element_and_wait(OrderPageLocators.ORDER_DETAILS_POP_UP)
        assert order_pop_up.is_displayed()

    @allure.title("Test log in and make order")
    def test_log_in_and_make_order(self, driver, random_user):
        order_page = OrderPage(driver)
        my_account_page = MyAccountPage(driver)
        constructor_page = ConstructorPage(driver)
        my_account_page.create_user_and_login(random_user['email'], random_user['password'])
        constructor_page.add_click_on_order_button_and_drag_and_drop()
        order_page.click_on_make_order_button()
        pop_up = order_page.find_element_and_wait(OrderPageLocators.ORDER_MADE_POP_UP)
        assert pop_up.is_displayed()

    @allure.title("Test log in, make order and check order counter raise")
    def test_log_in_make_order_and_check_order_counter_raise(self, driver, create_user_and_login, random_user):
        order_page = OrderPage(driver)
        my_account_page = MyAccountPage(driver)
        constructor_page = ConstructorPage(driver)
        before = int(order_page.get_before())
        my_account_page.create_user_and_login(random_user['email'], random_user['password'])
        constructor_page.add_click_on_order_button_and_drag_and_drop()
        order_page.click_on_make_order_button()
        after = int(order_page.get_after())
        assert after > before

    @allure.title("Test log in, make order and check today's order counter raise")
    def test_log_in_make_order_and_check_order_today_counter_raise(self, driver, create_user_and_login, random_user):
        order_page = OrderPage(driver)
        my_account_page = MyAccountPage(driver)
        constructor_page = ConstructorPage(driver)
        before = int(order_page.get_before_today())
        my_account_page.create_user_and_login(random_user['email'], random_user['password'])
        constructor_page.add_click_on_order_button_and_drag_and_drop()
        order_page.click_on_make_order_button()
        after = int(order_page.get_after())
        assert after > before

    @allure.title("Test log in, make order and check order in in-progress feed")
    def test_log_in_make_order_and_check_order_in_in_progress_feed(self, driver, create_user_and_login, random_user):
        order_page = OrderPage(driver)
        my_account_page = MyAccountPage(driver)
        constructor_page = ConstructorPage(driver)
        my_account_page.create_user_and_login(random_user['email'], random_user['password'])
        constructor_page.add_click_on_order_button_and_drag_and_drop()
        order_page.click_on_make_order_button()
        order_id = order_page.get_order_id()
        order_page.click_on_order_made_button()
        assert order_id in order_page.get_text_from_element(OrderPageLocators.ORDER_PROGRESS_FEED)
