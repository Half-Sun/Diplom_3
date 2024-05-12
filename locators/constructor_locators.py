from selenium.webdriver.common.by import By


class ConstructorLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]'
    GO_TO_MY_ACCOUNT = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]'
    BURGER_TEXT = By.CSS_SELECTOR, 'h1.text.text_type_main-large.mb-5.mt-10'
    FIRST_INGREDIENT = By.CSS_SELECTOR, "ul.BurgerIngredients_ingredients__list__2A-mT > a.BurgerIngredient_ingredient__1TVf6:nth-of-type(1)"
    INGREDIENT_DETAILS_POP_UP = By.CSS_SELECTOR, 'section.Modal_modal_opened__3ISw4'
    INGREDIENT_DETAILS_POP_UP_CLOSE_BUTTON = By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK"
    BASKET_LIST = (By.CSS_SELECTOR, 'li.BurgerConstructor_basket__listItem__aWMu1.mr-4')
    INGREDIENT_COUNTER = By.CSS_SELECTOR, 'p.counter_counter__num__3nue1'
