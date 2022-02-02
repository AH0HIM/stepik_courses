from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        self.should_be_same_products_in_basket_and_on_the_page()
        self.should_be_correct_price_in_basket()
        self.should_be_success_message()

    def should_be_add_to_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Button 'Add to basket' is not presented"

    def click_add_to_cart_button(self):
        assert self.click_button(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to cart button can't click"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is not disappeared"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Message of Success added product in basket not found "

    def should_be_same_products_in_basket_and_on_the_page(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_of_added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert name_of_product == name_of_added_product, \
            "name of product and of the added to basket product are not same"

    def should_be_correct_price_in_basket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert product_cost == basket_price, \
            "product cost and basket price are not same"
