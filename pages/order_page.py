import time
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

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

    @allure.step("Get before")
    def get_before(self):
        self.click_on_order_feed()
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER))
        return before

    @allure.step("Get before")
    def get_after(self):
        self.find_element_and_wait(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        after = int(self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP))
        return after

    @allure.step("Get before today")
    def get_before_today(self):
        self.click_on_order_feed()
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        before = int(self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNTER))
        return before

    @allure.step("Get order id")
    def get_order_id(self):
        self.find_element_and_wait(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        self.wait_for_text_to_change(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP, "9999")
        order_id = self.get_text_from_element(OrderPageLocators.ORDERS_ALL_TIME_COUNTER_IN_POP_UP)
        return order_id

    @allure.step("Click on order button")
    def click_on_make_order_button(self):
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Click on close order button")
    def click_on_order_made_button(self):
        self.find_element_and_wait(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_MADE_CLOSE_BUTTON)
        self.click_on_order_feed()
