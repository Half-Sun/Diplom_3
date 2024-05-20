from selenium.webdriver.common.by import By


class MyAccountLocators:
    GO_TO_MY_ACCOUNT = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]'
    RESTORE_PASSWORD_BUTTON = By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/forgot-password"]'
    RESTORE_PASSWORD_EMAIL_FIELD = By.CSS_SELECTOR, "label.input__placeholder.text.noselect.text_type_main-default"
    RESTORE_PASSWORD_EMAIL_FIELD_INPUT = By.CSS_SELECTOR, ("input.text.input__textfield.text_type_main-default["
                                                           "type='text'][name='name']")
    RESTORE_PASSWORD_RESTORE_BUTTON = By.CSS_SELECTOR, (
        "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    RESTORE_PASSWORD_REMEMBER_PASSWORD_LINK = By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']"
    RESTORE_PASSWORD_NEW_PASSWORD_INPUT = By.CSS_SELECTOR, "div.input_type_password > input.input__textfield"
    RESTORE_PASSWORD_SHOW_PASSWORD_BUTTON = By.CSS_SELECTOR, "div.input__icon.input__icon-action"
    RESTORE_PASSWORD_NEW_PASSWORD_INPUT_SHOWN = By.CSS_SELECTOR, ("div.input__container input[type='text']["
                                                                  "name='Введите новый пароль']")

    MY_ACCOUNT_PASSWORD_FIELD = By.CSS_SELECTOR, ('input.text.input__textfield.text_type_main-default['
                                                  'type="password"][name="Пароль"]')
    MY_ACCOUNT_ENTER_BUTTON = By.CSS_SELECTOR, ("button.button_button__33qZ0.button_button_type_primary__1O7Bx"
                                                ".button_button_size_medium__3zxIa")
    MY_ACCOUNT_TEXT = By.CSS_SELECTOR, "p.Account_text__fZAIn.text.text_type_main-default"
    MY_ACCOUNT_ORDERS_HISTORY = By.CSS_SELECTOR, "a.Account_link__2ETsJ[href='/account/order-history']"
    MY_ACCOUNT_EXIT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"
