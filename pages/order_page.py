import time
import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from helpers import create_user_and_login


class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def execute(self, driver_command, params=None):
        return self.driver.execute(driver_command, params)

    @allure.step("Click on order feed")
    def click_on_order_feed(self):
        self.go_to_site()
        self.click_on_element(OrderPageLocators.ORDER_FEED_BUTTON)
        feed_text = self.get_text_from_element(OrderPageLocators.ORDER_FEED_TEXT)
        return feed_text

    @allure.step("Click on order to open")
    def click_on_order_to_open(self):
        self.go_to_site()
        self.click_on_element(OrderPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_FEED_LIST)

    @allure.step("Log in and make order")
    def log_in_and_make_order(self, random_user):
        create_user_and_login(self.driver, random_user)
        self.click_on_element(OrderPageLocators.ORDER_CONSTRUCTOR_BUTTON)
        self.drag_and_drop(OrderPageLocators.ORDER_FIRST_INGREDIENT, OrderPageLocators.ORDER_BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Check order counter")
    def check_order_counter(self, random_user):
        self.click_on_order_feed()
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER))
        create_user_and_login(self.driver, random_user)
        self.click_on_element(OrderPageLocators.ORDER_CONSTRUCTOR_BUTTON)
        self.drag_and_drop(OrderPageLocators.ORDER_FIRST_INGREDIENT, OrderPageLocators.ORDER_BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.find_element_and_wait(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        after = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP))
        return before, after

    @allure.step("Check today order counter")
    def check_today_order_counter(self, random_user):
        self.click_on_order_feed()
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNTER))
        create_user_and_login(self.driver, random_user)
        self.click_on_element(OrderPageLocators.ORDER_CONSTRUCTOR_BUTTON)
        self.drag_and_drop(OrderPageLocators.ORDER_FIRST_INGREDIENT, OrderPageLocators.ORDER_BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.find_element_and_wait(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        after = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP))
        return before, after

    @allure.step("Check order ID in progress feed")
    def check_order_id_in_in_progress_feed(self, random_user, driver):
        self.click_on_order_feed()
        create_user_and_login(self.driver, random_user)
        self.click_on_element(OrderPageLocators.ORDER_CONSTRUCTOR_BUTTON)
        self.drag_and_drop(OrderPageLocators.ORDER_FIRST_INGREDIENT, OrderPageLocators.ORDER_BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.find_element_and_wait(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        order_id = self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.find_element_and_wait(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_order_feed()
        return order_id
