import time

import allure

from locators.constructor_locators import ConstructorLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from conftest import driver, random_user


class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def execute(self, driver_command, params=None):
        return self.driver.execute(driver_command, params)

    @allure.step("Click on Order Feed button")
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
        self.go_to_site()
        self.create_user_and_login(random_user)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Check order counter")
    def check_order_counter(self, random_user):
        self.click_on_order_feed()
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER))
        self.create_user_and_login(random_user)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        time.sleep(10)
        after = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP))
        return before, after

    @allure.step("Check today order counter")
    def check_today_order_counter(self, random_user):
        self.click_on_order_feed()
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNTER))
        self.create_user_and_login(random_user)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_order_feed()
        time.sleep(10)
        after = int(self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNTER))
        return before, after

    @allure.step("Check order ID in in-progress feed")
    def check_order_id_in_in_progress_feed(self, random_user, driver):
        self.click_on_order_feed()
        self.create_user_and_login(random_user)
        self.click_on_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        self.drag_and_drop(ConstructorLocators.FIRST_INGREDIENT, ConstructorLocators.BASKET_LIST)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        time.sleep(10)
        order_id = self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.find_element_and_wait(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_order_feed()
        return order_id
