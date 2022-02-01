from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def add_product_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_description()

        self.should_be_add_button()
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()

        # self.solve_quiz_and_get_code()

        # self.should_be_success()
        # self.check_success_message()
        # self.should_be_product_in_basket(self.product_name)
        # self.should_be_same_price(self.product_price)

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return self.product_name

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return self.product_price

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button 'Add to basket' is not presented"

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Message of Success added product in basket not found "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"
        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"

    def should_be_product_in_basket(self, product_name):
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name == added_book_name.text, \
            f"book name is {product_name}, but added book name is {added_book_name.text}"

    def should_be_same_price(self, product_price):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert product_price == added_product_price.text, \
            f"book name is {product_price}, but added book name is {added_product_price.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is not disappeared"

    # def should_be_btn_add_to_basket(self):
    #     button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    #     button.click()
    #
    # def should_be_correctly_added_product_name(self):
    #     added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
    #     assert product_name.text == added_product_name.text, "Product name is not correct"
    #
    # def should_be_correctly_added_product_price(self):
    #     added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
    #     assert product_price.text == added_product_price.text, "Product price is not correct"

