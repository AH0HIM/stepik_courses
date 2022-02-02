from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_ADDRESS = (By.CSS_SELECTOR, ".form-control[id='id_registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, ".form-control[id='id_registration-password1']")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, ".form-control[id='id_registration-password2']")
    BTN_REGISTRATION = (By.CSS_SELECTOR, ".btn[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description + p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div:nth-of-type(1) > .alertinner > strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
