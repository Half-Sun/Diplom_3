import allure
import pytest
from conftest import driver, random_user
from locators.constructor_locators import ConstructorLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Test go to order feed")
    def test_go_to_order_feed(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order_feed()
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
        order_page.log_in_and_make_order(random_user)
        pop_up = order_page.find_element_and_wait(OrderPageLocators.ORDER_MADE_POP_UP)
        assert pop_up.is_displayed()

    @allure.title("Test log in, make order, and check order counter raise")
    def test_log_in_make_order_and_check_order_counter_raise(self, driver, random_user):
        order_page = OrderPage(driver)
        before, after = order_page.check_order_counter(random_user)
        assert after > before

    @allure.title("Test log in, make order, and check today order counter raise")
    def test_log_in_make_order_and_check_order_today_counter_raise(self, driver, random_user):
        order_page = OrderPage(driver)
        before, after = order_page.check_today_order_counter(random_user)
        assert after > before

    @allure.title("Test log in, make order, and check order in progress feed")
    def test_log_in_make_order_and_check_order_in_in_progress_feed(self, driver, random_user):
        order_page = OrderPage(driver)
        order_id = order_page.check_order_id_in_in_progress_feed(random_user,driver)
        assert order_id in order_page.get_text_from_element(OrderPageLocators.ORDER_PROGRESS_FEED)
