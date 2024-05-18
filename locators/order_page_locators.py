from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_FEED_BUTTON = By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/feed"]'
    ORDER_FEED_TEXT = By.CSS_SELECTOR, '.text.text_type_main-large.mt-10.mb-5'
    MAKE_ORDER_BUTTON = By.CSS_SELECTOR, 'button.button_button__33qZ0'
    ORDER_MADE_POP_UP = By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X"
    ORDER_FEED_LIST = By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59 > li:nth-of-type(1)"
    ORDER_DETAILS_POP_UP = By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi"
    ORDERS_ALL_TIME_COUNTER = By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ"
    ORDERS_ALL_TIME_COUNTER_IN_POP_UP = By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m"
    ORDERS_TODAY_COUNTER = By.CSS_SELECTOR, ("div.OrderFeed_ordersData__1L6Iv > div:nth-child(3) > "
                                             "p.OrderFeed_number__2MbrQ.text.text_type_digits-large")
    ORDER_MADE_CLOSE_BUTTON = By.CLASS_NAME, "Modal_modal__close_modified__3V5XS"
    ORDER_PROGRESS_FEED = By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text.text_type_digits-default.mb-2"
    ORDER_CONSTRUCTOR_BUTTON = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]'
    ORDER_FIRST_INGREDIENT = By.CSS_SELECTOR, "ul.BurgerIngredients_ingredients__list__2A-mT > a.BurgerIngredient_ingredient__1TVf6:nth-of-type(1)"
    ORDER_BASKET_LIST = By.CSS_SELECTOR, 'li.BurgerConstructor_basket__listItem__aWMu1.mr-4'
    ORDER_TO_MY_ACCOUNT = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]'
